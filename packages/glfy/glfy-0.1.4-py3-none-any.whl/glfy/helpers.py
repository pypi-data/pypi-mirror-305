# glfy_tool/helpers.py
import os
import logging
import shutil
import subprocess
from glfy_tool.config import FONTS_DIR, DEFAULT_ASCII_CHARS

def log_setup():
    """Setup custom logging format."""
    logging.basicConfig(level=logging.INFO, format='%(message)s')

def sanitize_ascii_chars(ascii_chars):
    """Ensure ASCII characters are sorted from dark to light."""
    # Optional: Implement any sanitization or sorting if needed
    return ascii_chars

def convert_resolution_string(resolution):
    """Convert resolution string 'WIDTHxHEIGHT' to integers."""
    try:
        width, height = map(int, resolution.lower().split('x'))
        return width, height
    except ValueError:
        raise ValueError("Resolution must be in the format WIDTHxHEIGHT, e.g., 1920x1080.")

def validate_resolution_option(resolution):
    """Validate and parse the resolution option."""
    width, height = convert_resolution_string(resolution)
    if width <= 0 or height <= 0:
        raise ValueError("Resolution dimensions must be positive integers.")
    return width, height

def is_image_file(file_path):
    """Check if the file is an image based on its extension."""
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp')
    return file_path.lower().endswith(image_extensions)

def is_video_file(file_path):
    """Check if the file is a video based on its extension."""
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm', '.3gp')
    return file_path.lower().endswith(video_extensions)

def clean_up(files_to_delete, dirs_to_delete):
    """Delete intermediate files and directories."""
    logging.info("Cleaning up intermediate files...")
    for file_path in files_to_delete:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
    for dir_path in dirs_to_delete:
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path, ignore_errors=True)

def execute_ffmpeg_command(command):
    """Run an FFmpeg command with error handling, suppressing FFmpeg output."""
    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"FFmpeg command failed: {e}")
        return False

def execute_ffmpeg_with_fallback(primary_command, fallback_command):
    """
    Attempt to run the primary FFmpeg command. If it fails, run the fallback command.

    Parameters:
    - primary_command: List of strings representing the primary FFmpeg command.
    - fallback_command: List of strings representing the fallback FFmpeg command.

    Returns:
    - True if either command succeeds.
    - False if both commands fail.
    """
    try:
        subprocess.run(primary_command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        try:
            subprocess.run(fallback_command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except subprocess.CalledProcessError as e:
            logging.error(f"FFmpeg command failed: {e}")
            return False
