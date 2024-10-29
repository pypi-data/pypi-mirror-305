# glfy/ascii_conversion.py

from .glfy_imports import *
from .utils import create_background, apply_background_removal, adaptive_enhance_image

def vectorized_color_adjustment(pixels, lightness_boost, vibrancy_boost):
    """
    Apply lightness and vibrancy boosts to an array of RGB pixels using OpenCV's optimized functions.

    Parameters:
    - pixels: NumPy array of shape (height, width, 3) with RGB values in [0, 255].
    - lightness_boost: Float multiplier for lightness.
    - vibrancy_boost: Float multiplier for vibrancy (saturation).

    Returns:
    - Adjusted pixels as a NumPy array with RGB values in [0, 255].
    """
    # Convert RGB to HLS
    hls = cv2.cvtColor(pixels, cv2.COLOR_RGB2HLS).astype(np.float32)

    # Apply boosts
    hls[:, :, 1] = np.clip(hls[:, :, 1] * lightness_boost, 0, 255)  # Lightness channel
    hls[:, :, 2] = np.clip(hls[:, :, 2] * vibrancy_boost, 0, 255)   # Saturation channel

    # Convert back to RGB
    rgb_adjusted = cv2.cvtColor(hls.astype(np.uint8), cv2.COLOR_HLS2RGB)

    return rgb_adjusted

def render_char_to_image(char, font, color, step_x, step_y):
    """
    Render a single ASCII character to an RGBA image of given size and color.
    """
    char_img = Image.new('RGBA', (step_x, step_y), (0, 0, 0, 0))
    draw = ImageDraw.Draw(char_img)
    draw.text((0, 0), char, font=font, fill=color)
    return np.array(char_img)

def create_ascii_overlay(ascii_matrix, pixels, font, step_x, step_y, black_and_white=False):
    """
    Create an optimized ASCII overlay image using batch rendering and caching.

    Parameters:
    - ascii_matrix: 2D NumPy array of ASCII characters.
    - pixels: 3D NumPy array of RGB pixels corresponding to each character.
    - font: PIL ImageFont object.
    - step_x: Horizontal spacing per character.
    - step_y: Vertical spacing per character.
    - black_and_white: If True, render characters in white color.

    Returns:
    - PIL Image object with ASCII characters rendered.
    """
    num_chars_y, num_chars_x = ascii_matrix.shape
    overlay_array = np.zeros((step_y * num_chars_y, step_x * num_chars_x, 4), dtype=np.uint8)

    # Cache for rendered characters as a batch
    char_cache = {}

    # Pre-render frequently used characters for different colors
    for y in range(num_chars_y):
        for x in range(num_chars_x):
            ascii_char = ascii_matrix[y, x]
            color = (255, 255, 255) if black_and_white else tuple(pixels[y, x])

            # Use character and color as the cache key
            cache_key = (ascii_char, color)

            if cache_key not in char_cache:
                # Render character if not in cache
                char_img = Image.new('RGBA', (step_x, step_y), (0, 0, 0, 0))
                draw = ImageDraw.Draw(char_img)
                draw.text((0, 0), ascii_char, font=font, fill=color)

                # Convert to NumPy array and cache the result
                char_cache[cache_key] = np.array(char_img)

            # Insert cached character image into overlay array
            overlay_array[y * step_y:(y + 1) * step_y, x * step_x:(x + 1) * step_x] = char_cache[cache_key]

    # Convert overlay array to a PIL image
    overlay = Image.fromarray(overlay_array, 'RGBA')
    return overlay

def image_to_ascii_art(
    image, brightness_boost, contrast_boost,
    lightness_boost, vibrancy_boost, gamma,
    horizontal_spacing, vertical_spacing, ascii_chars,
    background_vibrancy, background_brightness, background_blur_radius,
    font, black_and_white=False, background_removal=False,
    selfie_segmentation=None
):
    """Convert an image to ASCII art, maintaining original size."""
    
    if background_removal and selfie_segmentation:
        image = apply_background_removal(image, selfie_segmentation)

    # Convert PIL image to NumPy array immediately for OpenCV processing
    image_np = np.array(image)

    # Enhance the image brightness and contrast only if boost values are not zero
    if brightness_boost != 0.0 or contrast_boost != 0.0:
        image_np = adaptive_enhance_image(image_np, brightness_boost, contrast_boost)

    original_height, original_width = image_np.shape[:2]
    step_x = horizontal_spacing
    step_y = vertical_spacing

    num_chars_x = max(1, int(original_width / step_x))
    num_chars_y = max(1, int(original_height / step_y))

    # Resize image to new_width and new_height using OpenCV
    resized_image_np = cv2.resize(image_np, (num_chars_x, num_chars_y), interpolation=cv2.INTER_LINEAR)

    if black_and_white:
        pixels_gray = np.mean(resized_image_np, axis=2, keepdims=True).astype(np.uint8)
        adjusted_pixels = np.repeat(pixels_gray, 3, axis=2)
    else:
        # Use OpenCV for color adjustment
        adjusted_pixels = vectorized_color_adjustment(resized_image_np, lightness_boost, vibrancy_boost)

    grayscale = 0.299 * adjusted_pixels[..., 0] + 0.587 * adjusted_pixels[..., 1] + 0.114 * adjusted_pixels[..., 2]
    corrected_brightness = ((grayscale / 255.0) ** (1.0 / gamma)) * 255
    ascii_indices = ((1 - (corrected_brightness / 255)) * (len(ascii_chars) - 1)).astype(int)

    ascii_chars_arr = np.array(list(ascii_chars))
    ascii_matrix = ascii_chars_arr[ascii_indices]

    # Create the background image only if background parameters are not zero
    if background_vibrancy != 0.0 or background_brightness != 0.0 or background_blur_radius != 0:
        background_image = create_background(
            image_np, num_chars_x * step_x, num_chars_y * step_y,
            background_vibrancy, background_brightness, background_blur_radius
        )
    else:
        background_image = np.zeros((num_chars_y * step_y, num_chars_x * step_x, 3), dtype=np.uint8)

    ascii_overlay = create_ascii_overlay(ascii_matrix, adjusted_pixels, font, step_x, step_y, black_and_white)

    # Convert background and overlay to RGBA
    background_image = Image.fromarray(background_image).convert('RGBA')
    ascii_overlay = ascii_overlay.convert('RGBA')

    # Composite the ASCII overlay on the background
    try:
        ascii_image = Image.alpha_composite(background_image, ascii_overlay)
    except ValueError as e:
        logging.error(f"Images do not match: {e}")
        raise

    return ascii_image.convert('RGB')

def process_batch_frames(batch_files, frame_dir,
    brightness_boost, contrast_boost,
    lightness_boost, vibrancy_boost,
    gamma, horizontal_spacing, vertical_spacing,
    ascii_chars,
    background_vibrancy, background_brightness, background_blur_radius,
    font, black_and_white=False, background_removal=False
):
    """Process a batch of frames."""
    for file_name in batch_files:
        process_frame(
            file_name, frame_dir,
            brightness_boost, contrast_boost,
            lightness_boost, vibrancy_boost,
            gamma, horizontal_spacing, vertical_spacing,
            ascii_chars,
            background_vibrancy,
            background_brightness,
            background_blur_radius,
            font,
            black_and_white,
            background_removal
        )

def worker_init(background_removal_enabled):
    """Initializer function for multiprocessing Pool workers."""
    global selfie_segmentation
    if background_removal_enabled:
        import mediapipe as mp
        mp_selfie_segmentation = mp.solutions.selfie_segmentation
        selfie_segmentation = mp_selfie_segmentation.SelfieSegmentation(model_selection=0)
    else:
        selfie_segmentation = None

def convert_frames_to_ascii_art(
    frame_dir, brightness_boost, contrast_boost,
    lightness_boost, vibrancy_boost, gamma, ascii_chars,
    horizontal_spacing, vertical_spacing,
    background_vibrancy, background_brightness, background_blur_radius,
    font,
    black_and_white=False,
    background_removal=False
):
    """Convert frames to ASCII art using multiprocessing with batch processing."""
    frame_files = sorted([f for f in os.listdir(frame_dir) if f.endswith('.png')])

    # Set the number of processes and batch size internally
    max_processes = max(1, int(cpu_count() / 4))
    batch_size = 10

    # Split frame_files into batches
    batches = [frame_files[i:i + batch_size] for i in range(0, len(frame_files), batch_size)]

    # Create a pool of worker processes with an initializer
    with Pool(processes=max_processes, initializer=worker_init, initargs=(background_removal,)) as pool:
        pool.starmap(
            process_batch_frames,
            [
                (
                    batch,
                    frame_dir,
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
                    background_removal
                )
                for batch in batches
            ]
        )

def combine_ascii_frames_to_video(frame_dir, output_video_path, fps):
    """Combine ASCII frames into a video using h264_nvenc or fallback to libx264."""
    logging.info("Combining ASCII frames into video...")
    
    # Create a temporary directory to hold sequentially named frames
    sequential_dir = os.path.join(frame_dir, "sequential")
    os.makedirs(sequential_dir, exist_ok=True)

    # Rename frames to 'frame_%04d.png' sequentially
    sequential_files = sorted([f for f in os.listdir(frame_dir) if f.startswith('frame_') and f.endswith('.png')])
    for index, file_name in enumerate(sequential_files, start=1):
        src = os.path.join(frame_dir, file_name)
        dst = os.path.join(sequential_dir, f"frame_{index:04d}.png")
        shutil.move(src, dst)

    frame_path_pattern = os.path.join(sequential_dir, "frame_%04d.png")
    
    # Primary command using h264_nvenc
    primary_command = [
        "ffmpeg", "-y", "-framerate", str(fps), "-i", frame_path_pattern,
        "-c:v", "h264_nvenc",    # Hardware-accelerated encoder
        "-preset", "p7",         # Speed preset optimized for fastest encoding
        "-profile:v", "high",    # High profile for better quality
        "-pix_fmt", "yuv444p",   # Preserve color information
        "-b:v", "10M",           # Set bitrate to 10 Mbps (example)
        "-threads", "0",         # Utilize all available CPU cores
        output_video_path
    ]
    
    # Fallback command using libx264 with -tune animation
    fallback_command = [
        "ffmpeg", "-y", "-framerate", str(fps), "-i", frame_path_pattern,
        "-c:v", "libx264",         # Software encoder
        "-preset", "veryslow",     # Slower encoding with better compression
        "-crf", "18",              # Quality control (lower CRF for higher quality)
        "-profile:v", "high",      # High profile for better quality
        "-pix_fmt", "yuv444p",     # Preserve color information
        "-tune", "animation",      # Tune for animations
        "-threads", "0",           # Utilize all available CPU cores
        output_video_path
    ]
    
    success = execute_ffmpeg_with_fallback(primary_command, fallback_command)
    if not success:
        logging.error("Error combining frames into video with both encoders.")
    
    # Clean up the sequential frames directory
    shutil.rmtree(sequential_dir, ignore_errors=True)

def merge_audio_with_ascii_video(ascii_video, audio_path, final_output):
    """Combine the ASCII video with the original audio."""
    logging.info("Merging audio with ASCII video...")
    if audio_path:
        success = execute_ffmpeg_command([
            "ffmpeg", "-y", "-i", ascii_video, "-i", audio_path,
            "-c:v", "copy", "-c:a", "aac", "-b:a", "320k", "-strict", "experimental", "-threads", "0",
            final_output
        ])  # Set highest bitrate and utilize all CPU cores
        if success:
            logging.info(f"Final video with audio saved to {final_output}.")
        else:
            logging.error("Failed to merge audio with ASCII video.")
    else:
        # If there's no audio, just copy the video
        shutil.copy(ascii_video, final_output)
        logging.info("No audio to merge. Final video saved without audio.")

def process_frame(
    file_name, frame_dir,
    brightness_boost, contrast_boost,
    lightness_boost, vibrancy_boost,
    gamma, horizontal_spacing, vertical_spacing,
    ascii_chars,
    background_vibrancy, background_brightness, background_blur_radius,
    font, black_and_white=False, background_removal=False
):
    """Process a single frame."""
    frame_path = os.path.join(frame_dir, file_name)
    try:
        with Image.open(frame_path) as image:
            ascii_img = image_to_ascii_art(
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
                background_removal
            )
            ascii_img.save(frame_path)
    except Exception as e:
        logging.error(f"Error processing frame {file_name}: {e}")