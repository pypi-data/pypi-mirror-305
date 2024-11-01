# BertCC

BertCC is a context-aware Chinese text converter that uses BERT (Bidirectional Encoder Representations from Transformers) to convert Simplified Chinese (zh_CN) to Traditional Chinese (zh_TW). Unlike dictionary-based approaches, BertCC leverages the power of contextual understanding to provide more accurate conversions.

## Features

- **Context-Aware Conversion**: Utilizes BERT's contextual understanding to make intelligent conversion choices based on surrounding text
  ```
  Input:  他向师生发表演说
  BertCC: 他向師生發表演說  ✓
  OpenCC: 他向師生髮表演說  ✗
  ```

- **Configurable Processing**:
  - Adjustable batch size for optimal performance on different hardware
  - Configurable overlap between batches to maintain context across segments
  - Optional context prefix to guide conversion

- **Unlimited Text Length**: Processes text of any length through intelligent batch processing with overlap

- **Hardware Flexibility**: Supports both CPU and CUDA processing

- **Detailed Output Option**: Can show conversion probabilities and candidate selections when run in verbose mode

## Installation

```bash
pip install bertcc
```

## Usage

### Command Line Interface
```bash
# Basic usage
bertcc "要转换的文字" --batch-size 450 --overlap-size 50

# Using context prefix for proper nouns
bertcc "都是上里作的好事" -c "上里一將是人名。"
# Output: 都是上里作的好事  (preserves "上里" as a name instead of converting to "上裡")

# Show detailed conversion process
bertcc "他的头与发皆白" --verbose
```

### Python API
```python
from bertcc.converter import ConversionConfig, ChineseConverter

config = ConversionConfig(
    batch_size=450,
    overlap_size=50,
    context_prefix='上里一將是人名。',  # Context hint for proper nouns
    device="cuda",  # or "cpu"
    model_name="bert-base-chinese"
)

converter = ChineseConverter(config)
result = converter.convert("都是上里作的好事", show_details=True)
```

## Usage Considerations

### Input Text Quality

For optimal conversion results, consider these important guidelines:

1. **Pure Chinese Text Preferred**:
   ```
   Good: 他向师生发表演说

   Avoid: <div>他向师生发表演说</div>  // HTML tags may affect context
   ```

2. **Why This Matters**:
   - BERT models are trained primarily on natural Chinese text
   - Non-Chinese elements (HTML, markdown, special characters) can:
     - Disrupt the contextual understanding
     - Lead to incorrect character conversions
     - Break the natural language flow

3. **Best Practices**:
   - Clean input text of HTML/XML tags before conversion
   - Remove or minimize non-Chinese characters where possible
   - Keep formatting markup separate from text being converted
   - Use context prefix for proper nouns rather than special markers

4. **Handling Mixed Content**:
   If you must process text with mixed content:
   - Consider splitting the text into Chinese and non-Chinese segments
   - Process Chinese segments separately
   - Reassemble the text after conversion

## Configuration Options

| Parameter | Description | Default |
|-----------|-------------|---------|
| batch_size | Number of characters processed in each batch | 450 |
| overlap_size | Number of overlapping characters between batches | 50 |
| context_prefix | Optional prefix to provide additional context | '' |
| device | Computation device ("cuda" or "cpu") | "cuda" if available |
| model_name | BERT model to use for conversion | "bert-base-chinese" |

## How It Works

BertCC uses a unique approach to Chinese text conversion:

1. **Text Processing**:
   - Splits input text into manageable batches with overlap to maintain context
   - Identifies ambiguous characters that have multiple possible Traditional Chinese representations

2. **Masking and Prediction**:
   - Replaces ambiguous characters with BERT's [MASK] token
   - For example, "发" could be "發" (to express) or "髮" (hair)
   - The surrounding context helps BERT understand which meaning is intended

3. **Contextual Decision**:
   - BERT model predicts the most likely Traditional Chinese character for each mask
   - Predictions are influenced by:
     - Surrounding text context
     - Optional context prefix (useful for proper nouns)
     - Known character mappings and frequencies

4. **Batch Processing**:
   - Processes text in overlapping batches to handle long texts
   - Merges results while maintaining consistency at batch boundaries

## Limitations

1. **Phrase-Level Variations**: Cannot handle regional phrase differences between Simplified and Traditional Chinese due to its character-by-character processing architecture. For example:
   ```
   CN: 互联网        TW: 網際網路
   CN: 数据库        TW: 資料庫
   CN: 软件          TW: 軟體
   ```
   BertCC will convert these character-by-character (e.g., 互联网 → 互聯網) rather than using the regionally appropriate phrase (網際網路). This is because the model operates on character-level masking and prediction, not phrase-level transformation. For applications requiring region-specific terminology conversion, additional post-processing or a different approach would be needed.

2. **Computational Resources**: As a neural network-based solution, BertCC requires more computational resources compared to dictionary-based approaches like OpenCC.

3. **Processing Speed**: Due to the contextual analysis, conversion speed is slower than dictionary-based methods, though this is mitigated through batch processing.

## Comparison with Other Tools

Unlike traditional conversion tools like OpenCC that rely on character-to-character mapping, BertCC:
- Considers the entire context when making conversion decisions
- Handles ambiguous characters more accurately by understanding their usage
- Provides confidence scores for conversions in verbose mode
- Maintains contextual consistency across long texts through overlap processing

## Contributing

Contributions are welcome! Please feel free to submit pull requests, report issues, or suggest improvements.

## License

[Apache License 2.0](LICENSE)
