import argparse
import torch

from bertcc.converter import ConversionConfig
from bertcc.converter import ChineseConverter

def main():
    parser = argparse.ArgumentParser(description="A context-aware Simplified to Traditional Chinese converter using BERT")
    parser.add_argument("input_text", type=str, help="Text to convert")
    parser.add_argument("-b", "--batch-size", type=int, default=450, help="Number of characters per batch")
    parser.add_argument("-o", "--overlap-size", type=int, default=50, help="Number of overlapping characters between batches")
    parser.add_argument("-c", "--context-prefix", type=str, default='', help="Context prefix for conversion")
    parser.add_argument("-d", "--device", type=str, choices=["cpu", "cuda"], default="cuda" if torch.cuda.is_available() else "cpu", help="Device to use for computation")
    parser.add_argument("-m", "--model-name", type=str, default='bert-base-chinese', help="Bert model used for conversion")
    parser.add_argument("-v", "--verbose", action='store_true', help="Show detailed conversion output")

    args = parser.parse_args()

    config = ConversionConfig(
        batch_size=args.batch_size,
        overlap_size=args.overlap_size,
        context_prefix=args.context_prefix,
        model_name=args.model_name,
        device=args.device
    )

    converter = ChineseConverter(config)
    print(converter.convert(args.input_text, show_details=args.verbose))

if __name__ == "__main__":
    main()
