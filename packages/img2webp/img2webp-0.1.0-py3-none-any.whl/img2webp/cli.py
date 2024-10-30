import argparse
import logging
from pathlib import Path
from PIL import Image
from typing import List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def convert_image(
    input_path: str,
    output_path: str,
    quality: int = 80
) -> None:
    """
    Convert a single image to WebP format.
    
    Args:
        input_path: Path to input image
        output_path: Path to save WebP image
        quality: WebP quality (0-100)
    """
    try:
        image = Image.open(input_path)
        image.save(output_path, "WEBP", quality=quality)
        logging.info(f"Converted {input_path} to {output_path}")
    except Exception as e:
        logging.error(f"Failed to convert {input_path}: {e}")
        raise

def process_files(
    input_files: List[str],
    output_dir: str,
    quality: int = 80
) -> tuple[int, int]:
    """
    Process multiple image files.
    
    Args:
        input_files: List of input image paths
        output_dir: Directory to save converted images
        quality: WebP quality (0-100)
        
    Returns:
        Tuple of (successful conversions, failed conversions)
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    successful = 0
    failed = 0
    
    for input_file in input_files:
        input_path = Path(input_file)
        if input_path.suffix.lower() not in [".heic", ".jpg", ".jpeg", ".png"]:
            logging.warning(f"Skipping unsupported file: {input_file}")
            failed += 1
            continue
            
        output_file = output_path / f"{input_path.stem}.webp"
        
        try:
            convert_image(input_file, str(output_file), quality)
            successful += 1
        except Exception:
            failed += 1
    
    return successful, failed

def main() -> None:
    """Command line interface for img2webp."""
    parser = argparse.ArgumentParser(
        description="Convert images to WebP format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Convert a single file:
    img2webp-cli input.jpg -o output_dir
    
  Convert multiple files:
    img2webp-cli input1.jpg input2.png -o output_dir
    
  Set quality level:
    img2webp-cli input.jpg -o output_dir -q 90
    
  Convert all supported images in a directory:
    img2webp-cli directory/*.jpg -o output_dir
"""
    )
    
    parser.add_argument(
        "input",
        nargs="+",
        help="Input image file(s) or directory"
    )
    
    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Output directory for WebP files"
    )
    
    parser.add_argument(
        "-q", "--quality",
        type=int,
        default=80,
        choices=range(1, 101),
        metavar="[1-100]",
        help="WebP quality (1-100, default: 80)"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        successful, failed = process_files(args.input, args.output, args.quality)
        logging.info(f"Conversion complete: {successful} successful, {failed} failed")
        if failed > 0:
            exit(1)
    except Exception as e:
        logging.error(f"Conversion failed: {e}")
        exit(1)

if __name__ == "__main__":
    main()