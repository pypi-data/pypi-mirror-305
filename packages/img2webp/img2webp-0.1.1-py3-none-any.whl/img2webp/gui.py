import logging
import tkinter as tk
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
        """Create and layout the widgets."""
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.input_label = ttk.Label(self.frame, text="Input Files:")
        self.input_label.grid(row=0, column=0, sticky=tk.W)
        self.input_entry = ttk.Entry(self.frame, width=50)
        self.input_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
        self.input_button = ttk.Button(self.frame, text="Browse", command=self.select_input_files)
        self.input_button.grid(row=0, column=2, sticky=tk.W)

        self.output_label = ttk.Label(self.frame, text="Output Directory:")
        self.output_label.grid(row=1, column=0, sticky=tk.W)
        self.output_entry = ttk.Entry(self.frame, width=50)
        self.output_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))
        self.output_button = ttk.Button(self.frame, text="Browse", command=self.select_output_directory)
        self.output_button.grid(row=1, column=2, sticky=tk.W)

        self.compression_label = ttk.Label(self.frame, text="Compression Level:")
        self.compression_label.grid(row=2, column=0, sticky=tk.W)
        self.compression_slider = ttk.Scale(self.frame, from_=0, to=1, orient=tk.HORIZONTAL)
        self.compression_slider.set(DEFAULT_COMPRESSION)
        self.compression_slider.grid(row=2, column=1, sticky=(tk.W, tk.E))

        self.compression_value_label = ttk.Label(self.frame, text=f"{DEFAULT_COMPRESSION:.2f}")
        self.compression_value_label.grid(row=2, column=2, sticky=tk.W)
        self.compression_slider.bind("<Motion>", self.update_compression_value)

        self.help_button = ttk.Button(self.frame, text="?", command=self.show_help)
        self.help_button.grid(row=2, column=3, sticky=tk.W)
        self.help_button.bind("<Enter>", self.show_help_hover)
        self.help_button.bind("<Leave>", self.hide_help_hover)

        self.convert_button = ttk.Button(self.frame, text="Convert", command=self.convert_images)
        self.convert_button.grid(row=3, column=1, sticky=tk.E)

        self.progress_bar = ttk.Progressbar(self.frame, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress_bar.grid(row=4, column=0, columnspan=4, sticky=(tk.W, tk.E))
        self.progress_bar.grid_remove()  # Hide the progress bar initially

        self.status_bar = ttk.Label(self.frame, text="", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.grid(row=5, column=0, columnspan=4, sticky=(tk.W, tk.E))

        self.help_label = ttk.Label(self.frame, text="", foreground="gray")
        self.help_label.grid(row=6, column=0, columnspan=4, sticky=tk.W)

    def update_compression_value(self, event):
        """Update the compression value label."""
        self.compression_value_label.config(text=f"{self.compression_slider.get():.2f}")

    def select_input_files(self):
        """Select multiple input files."""
        self.input_files = filedialog.askopenfilenames(filetypes=[("Image files", "*.heic *.jpg *.jpeg *.png")])
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, "; ".join(self.input_files))

    def select_output_directory(self):
        """Select the output directory."""
        self.output_dir = filedialog.askdirectory()
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.output_dir)

    def convert_images(self):
        """Convert selected images to WebP format."""
        if not self.output_dir:
            messagebox.showerror("Error", "Please select an output directory.")
            return

        if not self.input_files:
            messagebox.showerror("Error", "Please select input files.")
            return

        if not any(Path(file).suffix.lower() in SUPPORTED_FORMATS for file in self.input_files):
            messagebox.showerror("Error", f"No supported images found. Supported formats: {', '.join(SUPPORTED_FORMATS)}")
            return

        self.progress_bar.grid()
        self.progress_bar.config(value=0)
        self.status_bar.config(text="Starting conversion...", background="yellow")
        self.root.update_idletasks()

        compression_level = self.compression_slider.get()
        total_files = len(self.input_files)
        converted_files = 0
        skipped_files = []

        for file in self.input_files:
            if Path(file).suffix.lower() in SUPPORTED_FORMATS:
                try:
                    self.convert_image_to_webp(file, self.output_dir, compression_level)
                    converted_files += 1
                    progress = (converted_files / total_files) * 100
                    self.progress_bar.config(value=progress)
                    self.status_bar.config(text=f"Converting... {progress:.2f}% complete", background="yellow")
                    self.root.update_idletasks()
                except Exception as e:
                    skipped_files.append((file, str(e)))

        if skipped_files:
            skipped_message = "The following files were skipped because:\n"
            for file, reason in skipped_files:
                skipped_message += f"{file}: {reason}\n"
            messagebox.showwarning("Conversion Completed with Skips", skipped_message)

        self.progress_bar.config(value=100)
        self.status_bar.config(text="Images successfully converted.", background="green")
        self.root.update_idletasks()

    def select_input_files(self):
        """Select multiple input files."""
        self.input_files = filedialog.askopenfilenames(filetypes=[("Image files", "*.heic *.jpg *.jpeg *.png")])
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, "; ".join(self.input_files))

    def select_output_directory(self):
        """Select the output directory."""
        self.output_dir = filedialog.askdirectory()
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.output_dir)

    def convert_image_to_webp(self, input_path, output_path, compression_level):
        """Convert a single image to WebP format."""
        image = Image.open(input_path)
        output_file = Path(output_path) / (Path(input_path).stem + ".webp")
        image.save(output_file, "WEBP", quality=int(compression_level * 100))
        logging.info(f"Converted {input_path} to {output_file}")

    def show_help(self):
        """Show help message."""
        messagebox.showinfo("Compression Level", "Adjust the slider to set the compression level for the WebP images. A lower value means higher compression and lower quality, while a higher value means lower compression and higher quality.")

    def show_help_hover(self, event):
        """Show help message on hover."""
        self.help_label.config(text="Adjust the slider to set the compression level.")

    def hide_help_hover(self, event):
        """Hide help message on hover leave."""
        self.help_label.config(text="")

def main():
    root = Tk()
    app = ImageConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()