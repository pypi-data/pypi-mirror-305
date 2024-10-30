# img2webp

A tool to convert images to WebP format with both GUI and CLI interfaces.

## Features

- Convert multiple images to WebP format
- Support for HEIC, JPG, JPEG, and PNG formats
- Adjustable compression/quality level
- Both GUI and CLI interfaces
- Progress tracking
- Batch processing support

## Installation

```bash
pip install img2webp
```

## Usage

### Graphical Interface

Run the GUI converter by executing:

```bash
img2webp
```

Or in Python:

```python
from img2webp.gui import main
main()
```

### Command Line Interface

The CLI version provides various options for converting images:

```bash
# Convert a single file
img2webp-cli input.jpg -o output_dir

# Convert multiple files
img2webp-cli input1.jpg input2.png -o output_dir

# Set quality level (1-100)
img2webp-cli input.jpg -o output_dir -q 90

# Convert all supported images in a directory
img2webp-cli directory/*.jpg -o output_dir

# Enable verbose output
img2webp-cli input.jpg -o output_dir -v
```

### Python API

You can also use the package programmatically:

```python
from img2webp import convert_image, process_files

# Convert a single image
convert_image("input.jpg", "output.webp", quality=80)

# Convert multiple images
successful, failed = process_files(
    ["input1.jpg", "input2.png"],
    "output_directory",
    quality=80
)
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.