"""
Image Resolution Detector
========================

This module provides functionality to determine the resolution (dimensions) of image files
using the Python Imaging Library (PIL).

Dependencies:
    - PIL (Python Imaging Library/Pillow)
    - Python 3.7+

Author: Prerak Pithadiya
Date: February 22, 2025
Version: 1.1
"""

import logging
from typing import Optional, Tuple
from pathlib import Path
from PIL import Image

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
DEFAULT_DPI = 72


def is_supported_format(image_path: str) -> bool:
    """
    Check if the image format is supported.

    Parameters:
    -----------
    image_path : str
        Path to the image file

    Returns:
    --------
    bool
        True if the format is supported, False otherwise
    """
    return any(image_path.lower().endswith(fmt) for fmt in SUPPORTED_FORMATS)


def get_image_resolution(image_path: str) -> Optional[Tuple[int, int]]:
    """
    Retrieve the resolution (width and height) of an image file.

    Parameters:
    -----------
    image_path : str
        The file path to the image. Supports various formats including JPG, PNG,
        BMP, and other formats supported by PIL.

    Returns:
    --------
    tuple or None
        A tuple containing (width, height) in pixels if successful.
        Returns None if there's an error reading the image.

    Raises:
    -------
    TypeError
        If image_path is not a string
    ValueError
        If image_path is empty or format not supported
    FileNotFoundError
        If the specified image file doesn't exist
    PIL.UnidentifiedImageError
        If the file is not a valid image format
    """
    # Input validation
    if not isinstance(image_path, str):
        raise TypeError("image_path must be a string")
    if not image_path.strip():
        raise ValueError("image_path cannot be empty")
    if not is_supported_format(image_path):
        raise ValueError(
            f"Unsupported image format. Supported formats are: {', '.join(SUPPORTED_FORMATS)}"
        )

    try:
        with Image.open(image_path) as img:
            logging.info(f"Successfully opened image: {image_path}")
            return img.size
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return None
    except Image.UnidentifiedImageError as e:
        logging.error(f"Invalid image format: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None


def get_image_info(image_path: str) -> Optional[dict]:
    """
    Get detailed information about an image file.

    Parameters:
    -----------
    image_path : str
        Path to the image file

    Returns:
    --------
    dict or None
        Dictionary containing image information including:
        - resolution
        - format
        - mode
        - size in bytes
    """
    try:
        with Image.open(image_path) as img:
            file_size = Path(image_path).stat().st_size
            return {
                "resolution": img.size,
                "format": img.format,
                "mode": img.mode,
                "size_bytes": file_size,
                "dpi": getattr(img, "info", {}).get("dpi", DEFAULT_DPI),
            }
    except Exception as e:
        logging.error(f"Error getting image info: {e}")
        return None


if __name__ == "__main__":
    # Single image test
    image_path = "img5.bmp"  # Replace with your image path

    try:
        # Check if file exists first
        if not Path(image_path).exists():
            print(f"Error: Image file '{image_path}' does not exist")
            exit()

        print("\n=== Image Resolution Analysis ===")
        # Get basic resolution
        resolution = get_image_resolution(image_path)
        if resolution:
            print(f"\nResolution: {resolution[0]} x {resolution[1]} pixels")

        # Get detailed information
        info = get_image_info(image_path)
        if info:
            print("\nDetailed Image Information:")
            for key, value in info.items():
                print(f"{key}: {value}")

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
