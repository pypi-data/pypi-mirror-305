from dataclasses import dataclass
from typing import List, Tuple, Dict

import logging
import os
import re
import sys
import torch
import torch.nn.functional as F
import unicodedata

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class ConversionConfig:
    """Configuration for text conversion"""
    batch_size: int = 450  # Characters per batch
    overlap_size: int = 50  # Overlap between batches
    context_prefix: str = ''
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    model_name: str = "bert-base-chinese"

class ChineseConverter:
    def __init__(self, config: ConversionConfig = None):
        self.config = config or ConversionConfig()
        self.model, self.tokenizer = self._load_model()
        self.device = self.config.device
        self.model = self.model.to(self.device)

    def _load_model(self):
        """Load the BERT model with error handling"""
        try:
            from transformers import AutoTokenizer, AutoModelForMaskedLM
            tokenizer = AutoTokenizer.from_pretrained(self.config.model_name)
            model = AutoModelForMaskedLM.from_pretrained(self.config.model_name)
            return model, tokenizer
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            raise

    def _split_into_batches(self, text: str) -> List[Tuple[str, int]]:
        """Split text into overlapping batches with position tracking"""
        batches = []
        pos = 0

        while pos < len(text):
            batch_end = min(pos + self.config.batch_size, len(text))
            batch_start = pos
            if pos != 0:
                batch_start -= self.config.overlap_size
            batch = text[batch_start:batch_end]
            batches.append(batch)
            pos += self.config.batch_size
        return batches

    def _process_batch(self, batch: str) -> Tuple[List[List[Tuple[str, float]]], str]:
        """Process a single batch with masks"""
        tc = []
        need_prefix = True
        need_mask = False

        # Convert characters and identify masks needed
        from bertcc.utils.constants import sc_dict
        from bertcc.utils.constants import tw_dict
        ascii_str = ''
        for s in batch:
            category = unicodedata.category(s)
            if not category in ('Lo', 'Lm', 'Mn', 'Mc', 'Me'):
                ascii_str += s
                continue
            if len(ascii_str) > 0:
                tc.append([ascii_str])
            ascii_str = ''
            if s in sc_dict:
                t = sc_dict[s]
                if len(t) > 1:
                    nt = t.copy()
                    nt.insert(0, s)
                    tc.append(nt)
                    need_mask = True
                    if not s in t:  # If simplified char isn't in traditional options
                        need_prefix = False
                else:
                    tc.append(t)
                    need_prefix = False  # Single mapping doesn't need prefix
            else:
                if s in tw_dict:
                    s = tw_dict[s]
                tc.append([s])
        if len(ascii_str) > 0:
            tc.append([ascii_str])
        if not need_mask:
            return [], ''.join([t[0] for t in tc])

        # Create masked text and candidates list
        text = ''
        candidates_list = []
        for t in tc:
            if len(t) == 1 or '[MASK]' in t:
                text += t[0]
            else:
                text += '[MASK]'
            count = t[0].count('[MASK]')
            if count > 0:
                while count != 0:
                    candidates_list.append([])
                    count = count - 1
                continue
            if len(t) > 1:
                candidates_list.append(t)

        # Only add prefix if needed
        prefix_len = 0
        if len(self.config.context_prefix) > 0:
            text = self.config.context_prefix + text
            prefix_len = len(self.config.context_prefix)
        elif need_prefix:
            text = '繁體說法：' + text
            prefix_len = 5

        return self._get_predictions(text, candidates_list, prefix_len)

    def _get_predictions(self, text: str, candidates_list: List[Tuple[str, int]], prefix_len: int) -> Tuple[List[List[Tuple[str, float]]], str]:
        """Get masked token predictions with context using batch processing"""
        try:
            results = []
            # Initial encoding
            inputs = self.tokenizer(text, return_tensors="pt")
            inputs = {k: v.to(self.device) for k, v in inputs.items()}

            # Find all mask positions upfront
            mask_positions = torch.where(inputs["input_ids"][0] == self.tokenizer.mask_token_id)[0]
            assert len(mask_positions) == len(candidates_list), "Please check if there is a [MASK] in the input or context prefix"

            # Get all predictions in one forward pass
            with torch.no_grad():
                outputs = self.model(**inputs)
                all_predictions = outputs.logits[0, mask_positions]

            # Process all masks without re-encoding
            for idx, candidates in enumerate(candidates_list):
                if len(candidates) == 0:
                    results.append([('[MASK]', 1.0)])
                    continue
                real_candidates = candidates.copy()
                real_candidates.pop(0)

                # Get probabilities for candidates
                candidate_ids = torch.tensor([
                    self.tokenizer.encode(c, add_special_tokens=False)[0]
                    for c in real_candidates
                ], device=self.device)

                # Calculate probabilities for all candidates at once
                candidate_predictions = all_predictions[idx][candidate_ids]
                candidate_probs = F.softmax(candidate_predictions, dim=0)

                # Store results
                mask_results = list(zip(real_candidates, candidate_probs.cpu().tolist()))
                max_i = -1
                max_p = -1.0
                for i, (_, p) in enumerate(mask_results):
                    if p > max_p:
                        p = max_p
                        max_i = i
                inputs['input_ids'][:, mask_positions[idx]] = candidate_ids[max_i]
                if idx < len(mask_positions) - 1 and mask_positions[idx].item() == mask_positions[idx + 1].item() - 1:
                    key = f'{candidates_list[idx][0]}{"" if len(candidates_list[idx + 1]) == 0 else candidates_list[idx + 1][0]}'
                    from bertcc.utils.constants import scp_set
                    if key in scp_set:
                        outputs = self.model(**inputs)
                        all_predictions = outputs.logits[0, mask_positions]
                mask_results.sort(key=lambda x: x[1], reverse=True)
                results.append(mask_results)

            # Remove prefix if it was added
            if prefix_len > 0:
                text = text[prefix_len:]
            return results, self._replace_matches(text, r'\[MASK\]', [p[0][0] for p in results])

        except Exception as e:
            logger.error(f"Error in prediction: {e}")
            raise

    def _replace_matches(self, text, pattern, replacement_list):
        """
        Replace each regex match in text with corresponding string from replacement_list.

        Args:
            text (str): Input text to process
            pattern (str): Regular expression pattern to match
            replacement_list (list): List of strings to use as replacements

        Returns:
            str: Text with all matches replaced
        """
        matches = re.finditer(pattern, text)
        result = text
        offset = 0
        for i, match in enumerate(matches):
            replacement = replacement_list[i]
            start = match.start() + offset
            end = match.end() + offset
            result = result[:start] + replacement + result[end:]
            offset += len(replacement) - (match.end() - match.start())
        return result

    def convert(self, input_str: str, show_details: bool = False) -> str:
        """Convert simplified Chinese text to traditional Chinese with batch processing"""
        if not input_str:
            return ""

        # Split into batches
        batches = self._split_into_batches(input_str)
        final_text = []

        # Process each batch
        for batch_id, batch_text in enumerate(batches):
            predictions, converted_text = self._process_batch(batch_text)
            half_overlap = self.config.overlap_size // 2
            if batch_id != len(batches) - 1:
                converted_text = converted_text[:-half_overlap]
            if batch_id != 0:
                converted_text = converted_text[half_overlap:]
            final_text.append(converted_text)

            if show_details and predictions:
                logger.info("\nProbabilities for candidates at each mask position:")
                for mask_idx, mask_predictions in enumerate(predictions):
                    logger.info(f"\nMask position {mask_idx + 1}:")
                    for word, prob in mask_predictions:
                        logger.info(f"{word}: {prob:.4f}")
        result = ''.join(final_text)
        assert len(input_str) == len(result)
        return ''.join(final_text)
