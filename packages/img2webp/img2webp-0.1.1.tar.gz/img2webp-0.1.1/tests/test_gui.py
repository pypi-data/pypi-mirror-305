import pytest
import tkinter as tk
from img2webp.gui import ImageConverterApp

@pytest.fixture
def root():
    """Create a Tk root instance."""
    root = tk.Tk()
    yield root
    root.destroy()

def test_app_creation(root):
    """Test that the app can be created."""
    app = ImageConverterApp(root)
    assert app is not None
    assert isinstance(app.root, tk.Tk)

def test_initial_values(root):
    """Test initial values of the app."""
    app = ImageConverterApp(root)
    assert app.input_files == []
    assert app.compression_slider.get() == 0.8  # Default compression value

def test_convert_button(root):
    """Test the convert button functionality."""
    app = ImageConverterApp(root)
    assert app.convert_button.cget("text") == "Convert"

