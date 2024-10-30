import pytest
from pathlib import Path
import tempfile
import shutil
from img2webp.cli import convert_image, process_files

@pytest.fixture
def temp_dir():
    """Create a temporary directory for test outputs."""
    temp_path = tempfile.mkdtemp()
    yield temp_path
    shutil.rmtree(temp_path)

@pytest.fixture
def test_images():
    """Get paths to test images."""
    test_data_dir = Path(__file__).parent / "test_data"
    return [str(p) for p in test_data_dir.glob("*.jpg")]

def test_convert_image(temp_dir, test_images):
    """Test converting a single image."""
    if not test_images:
        pytest.skip("No test images available")
    
    input_path = test_images[0]
    output_path = str(Path(temp_dir) / "output.webp")
    
    convert_image(input_path, output_path, quality=80)
    assert Path(output_path).exists()
    assert Path(output_path).stat().st_size > 0

def test_process_files(temp_dir, test_images):
    """Test processing multiple files."""
    if not test_images:
        pytest.skip("No test images available")
    
    successful, failed = process_files(test_images, temp_dir, quality=80)
    assert successful > 0
    assert failed == 0
    
    # Check if output files exist
    output_files = list(Path(temp_dir).glob("*.webp"))
    assert len(output_files) == successful

def test_invalid_input(temp_dir):
    """Test handling of invalid input files."""
    with pytest.raises(Exception):
        convert_image("nonexistent.jpg", str(Path(temp_dir) / "output.webp"))

def test_invalid_quality(temp_dir, test_images):
    """Test handling of invalid quality values."""
    if not test_images:
        pytest.skip("No test images available")
    
    with pytest.raises(Exception):
        convert_image(test_images[0], str(Path(temp_dir) / "output.webp"), quality=101)