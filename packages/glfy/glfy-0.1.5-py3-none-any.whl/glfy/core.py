# glfy/core.py

from .glfy_imports import *
from .video_processing import process_video
from .image_processing import process_image
from .live_video_processing import process_live_video
from .utils import (
    is_image_file,
    is_video_file
)

def process_source(
    scale_factor, fps, brightness_boost, contrast_boost,
    lightness_boost, vibrancy_boost, ascii_chars, gamma,
    horizontal_spacing, vertical_spacing, background_vibrancy, background_brightness,
    background_blur_radius, font, target_width=None, target_height=None,
    black_and_white=False, background_removal=False, source='scr',
    selfie_segmentation=None
):
    """Wrapper to process live video."""
    process_live_video(
        scale_factor, fps, brightness_boost, contrast_boost,
        lightness_boost, vibrancy_boost, ascii_chars, gamma,
        horizontal_spacing, vertical_spacing, background_vibrancy, background_brightness,
        background_blur_radius, font, target_width, target_height,
        black_and_white, background_removal, source, selfie_segmentation
    )

def process_input(
    input_path, scale_factor, fps, brightness_boost, contrast_boost,
    lightness_boost, vibrancy_boost, ascii_chars, gamma,
    horizontal_spacing, vertical_spacing, background_vibrancy, background_brightness,
    background_blur_radius, target_width, target_height,
    font, black_and_white=False, background_removal=False,
    selfie_segmentation=None
):
    """Determine the type of input and process accordingly."""
    if is_image_file(input_path):
        process_image(
            input_path, scale_factor, brightness_boost, contrast_boost,
            lightness_boost, vibrancy_boost, ascii_chars, gamma,
            horizontal_spacing, vertical_spacing,
            background_vibrancy, background_brightness, background_blur_radius,
            target_width, target_height,
            font, black_and_white, background_removal,
            selfie_segmentation
        )
    elif is_video_file(input_path):
        process_video(
            input_path, scale_factor, fps, brightness_boost, contrast_boost,
            lightness_boost, vibrancy_boost, ascii_chars, gamma,
            horizontal_spacing, vertical_spacing,
            background_vibrancy, background_brightness, background_blur_radius,
            target_width, target_height,
            font, black_and_white, background_removal,
            selfie_segmentation
        )
    else:
        logging.error("Error: Unsupported file format.")
