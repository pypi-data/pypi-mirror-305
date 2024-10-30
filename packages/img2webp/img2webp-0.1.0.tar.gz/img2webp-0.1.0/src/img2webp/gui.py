import logging
from tkinter import filedialog, messagebox, ttk, Tk, Scale, HORIZONTAL
from PIL import Image, ImageTk
from pathlib import Path
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Constants
DEFAULT_COMPRESSION = 0.8
SUPPORTED_FORMATS = [".heic", ".jpg", ".jpeg", ".png"]

class ImageConverterApp:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Image to WebP Converter")
        self.create_widgets()
        self.input_files = []

    def create_widgets(self):
        # Create and place widgets here
        self.compression_slider = Scale(self.root, from_=0, to=1, resolution=0.01, orient=HORIZONTAL)
        self.compression_slider.set(DEFAULT_COMPRESSION)
        self.compression_slider.pack()

def main():
    root = Tk()
    app = ImageConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()