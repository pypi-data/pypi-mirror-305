"""
img2webp - A tool to convert images to WebP format

This package provides both GUI and CLI interfaces for converting images to WebP format.
"""

from .cli import convert_image, process_files

__version__ = "0.1.0"
__all__ = ['convert_image', 'process_files']