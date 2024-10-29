# glfy/image_processing.py

from .glfy_imports import *
from .ascii_conversion import image_to_ascii_art
from .utils import convert_to_png

def process_image(
    input_path, scale_factor, brightness_boost, contrast_boost,
    lightness_boost, vibrancy_boost, ascii_chars, gamma,
    horizontal_spacing, vertical_spacing,
    background_vibrancy, background_brightness, background_blur_radius,
    target_width, target_height,
    font, black_and_white=False, background_removal=False,
    selfie_segmentation=None
):
    """Process a single image and convert it to ASCII art."""
    output_dir = os.path.dirname(input_path)
    original_filename = os.path.splitext(os.path.basename(input_path))[0]

    png_image = convert_to_png(input_path, output_dir)
    if not png_image:
        return

    try:
        with Image.open(png_image) as image:
            original_w, original_h = image.size
            target_ratio = target_width / target_height if target_width and target_height else original_w / original_h
            original_ratio = original_w / original_h

            if target_width and target_height:
                if original_ratio > target_ratio:
                    new_width = target_width
                    new_height = int(target_width / original_ratio)
                else:
                    new_height = target_height
                    new_width = int(target_height * original_ratio)
            else:
                new_width, new_height = original_w, original_h

            frame_np = np.array(image)

            # Resize using OpenCV
            frame_resized = cv2.resize(frame_np, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
            image = Image.fromarray(frame_resized)

            ascii_image = image_to_ascii_art(
                image,
                brightness_boost,
                contrast_boost,
                lightness_boost,
                vibrancy_boost,
                gamma,
                horizontal_spacing,
                vertical_spacing,
                ascii_chars,
                background_vibrancy,
                background_brightness,
                background_blur_radius,
                font,
                black_and_white,
                background_removal,
                selfie_segmentation
            )
            
            final_output = os.path.join(output_dir, f"{original_filename}_glfy.png")
            ascii_image.save(final_output)
            logging.info(f"ASCII art image saved to {final_output}.")

    except Exception as e:
        logging.error(f"Error processing image: {e}")

    finally:
        if os.path.exists(png_image):
            os.remove(png_image)
