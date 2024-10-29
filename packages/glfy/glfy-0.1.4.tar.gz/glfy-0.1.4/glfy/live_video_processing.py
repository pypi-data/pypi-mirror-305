# glfy/live_video_processing.py

from .glfy_imports import *
from .ascii_conversion import image_to_ascii_art

def pad_frame_to_target_size(frame, target_width, target_height):
    """Pad or resize the frame to match the target width and height."""
    height, width, _ = frame.shape

    # If the frame is larger than the target, resize it to fit within the target dimensions
    if width > target_width or height > target_height:
        frame = cv2.resize(frame, (target_width, target_height), interpolation=cv2.INTER_AREA)
        return frame

    # Calculate padding for height and width
    pad_top = max((target_height - height) // 2, 0)
    pad_bottom = max(target_height - height - pad_top, 0)
    pad_left = max((target_width - width) // 2, 0)
    pad_right = max(target_width - width - pad_left, 0)

    # Pad the frame with black borders if necessary
    padded_frame = cv2.copyMakeBorder(
        frame, pad_top, pad_bottom, pad_left, pad_right,
        cv2.BORDER_CONSTANT, value=[0, 0, 0]
    )

    return padded_frame

def process_live_video(
    scale_factor, fps, brightness_boost, contrast_boost,
    lightness_boost, vibrancy_boost, ascii_chars, gamma,
    horizontal_spacing, vertical_spacing, background_vibrancy, background_brightness,
    background_blur_radius, font, target_width=None, target_height=None,
    black_and_white=False, background_removal=False, source='scr',
    selfie_segmentation=None
):
    """Capture live video from the camera or screen and stream ASCII art to a virtual camera."""
    if source == 'ca':
        cap = cv2.VideoCapture(0)  # Open the default camera
        if not cap.isOpened():
            logging.error("Error: Could not open camera.")
            return

        # Use camera's resolution if target resolution is not specified
        if not target_width or not target_height:
            target_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            target_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Set the desired resolution if specified
        if target_width and target_height:
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, target_width)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, target_height)

        try:
            with pyvirtualcam.Camera(width=target_width,
                                     height=target_height,
                                     fps=fps,
                                     fmt=PixelFormat.BGR) as vcam:
                logging.info(f'Virtual camera device: {vcam.device}')
                running = True
                frame_queue = deque(maxlen=1)  # Create a frame queue with max length of 1

                def read_frames():
                    """Thread for reading frames from the camera."""
                    nonlocal running
                    while running:
                        ret, frame = cap.read()
                        if not ret:
                            logging.error("Error: Failed to capture video frame.")
                            break
                        # Add frame to the queue, replacing the old frame if full
                        frame_queue.append(frame)

                # Start the frame reading thread
                read_thread = threading.Thread(target=read_frames)
                read_thread.start()

                try:
                    while running:
                        if not frame_queue:
                            time.sleep(0.01)
                            continue  # Wait for frames to be available

                        # Get the latest frame from the queue
                        frame = frame_queue.pop()

                        # Convert the frame to RGB
                        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        pil_image = Image.fromarray(frame_rgb)

                        # Convert to ASCII art
                        ascii_image = image_to_ascii_art(
                            pil_image,
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

                        # Convert the ASCII image back to an OpenCV image
                        ascii_frame = cv2.cvtColor(np.array(ascii_image), cv2.COLOR_RGB2BGR)

                        # Pad the ASCII frame to match the target resolution
                        ascii_frame = pad_frame_to_target_size(ascii_frame, target_width, target_height)

                        # Send the frame to the virtual camera
                        vcam.send(ascii_frame)
                        vcam.sleep_until_next_frame()

                except KeyboardInterrupt:
                    logging.info("Virtual camera streaming interrupted by user.")
                    running = False

                finally:
                    running = False
                    read_thread.join()  # Wait for the frame reading thread to finish
                    cap.release()  # Release the camera
                    logging.info("Virtual camera streaming stopped. Exiting script.")

        except pyvirtualcam.CameraDeviceError as e:
            logging.error(f"Virtual camera error: {e}")

    elif source == 'sc':
        # Determine screen dimensions
        if target_width and target_height:
            screen_width = target_width
            screen_height = target_height
        else:
            with mss.mss() as sct_temp:
                monitor_settings = sct_temp.monitors[1]
                screen_width = monitor_settings["width"]
                screen_height = monitor_settings["height"]

        try:
            with pyvirtualcam.Camera(width=screen_width, height=screen_height, fps=fps, fmt=PixelFormat.BGR) as vcam:
                logging.info(f'Virtual camera device: {vcam.device}')
                running = True
                frame_queue = deque(maxlen=1)  # Create a frame queue with max length of 1

                def read_frames():
                    """Thread for reading frames from the screen."""
                    nonlocal running
                    try:
                        with mss.mss() as sct:
                            monitor_settings = sct.monitors[1]  # Capture the primary monitor
                            while running:
                                img = sct.grab(monitor_settings)
                                frame = np.array(img)
                                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                                frame_queue.append(frame)
                    except Exception as e:
                        logging.error(f"Error in read_frames thread: {e}")
                        running = False

                # Start the frame reading thread
                read_thread = threading.Thread(target=read_frames, daemon=True)
                read_thread.start()

                try:
                    while running:
                        if not frame_queue:
                            time.sleep(0.01)
                            continue  # Wait for frames to be available

                        # Get the latest frame from the queue
                        frame = frame_queue.pop()

                        # Convert the frame to RGB
                        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        pil_image = Image.fromarray(frame_rgb)

                        # Convert to ASCII art
                        ascii_image = image_to_ascii_art(
                            pil_image,
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

                        # Convert the ASCII image back to an OpenCV image
                        ascii_frame = cv2.cvtColor(np.array(ascii_image), cv2.COLOR_RGB2BGR)

                        # Pad the ASCII frame to match the target resolution
                        ascii_frame = pad_frame_to_target_size(ascii_frame, screen_width, screen_height)

                        # Send the frame to the virtual camera
                        vcam.send(ascii_frame)
                        vcam.sleep_until_next_frame()

                except KeyboardInterrupt:
                    logging.info("Virtual camera streaming interrupted by user.")
                    running = False

                except Exception as e:
                    logging.error(f"An error occurred: {e}")
                    running = False

                finally:
                    running = False
                    read_thread.join()  # Wait for the frame reading thread to finish
                    logging.info("Live ASCII streaming stopped. Exiting script.")

        except pyvirtualcam.CameraDeviceError as e:
            logging.error(f"Virtual camera error: {e}")
