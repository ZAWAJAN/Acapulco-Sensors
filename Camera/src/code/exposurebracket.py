from picamera2 import Picamera2, Preview
from time import sleep

# Initialize the camera
picam2 = Picamera2()

# Configure camera settings
camera_config = picam2.create_still_configuration()
picam2.configure(camera_config)

# Function to apply settings and discard initial frames
def apply_settings_and_discard_frames(picam2, exposure_time):
    # Set the framerate to be longer than the exposure time
    frame_duration = int(exposure_time * 1.25)
    picam2.set_controls({"FrameDurationLimits": (frame_duration, frame_duration)})

    # Set exposure time
    picam2.set_controls({"ExposureTime": exposure_time, "AnalogueGain": 1.0, "AwbEnable": True, "AwbMode": 4})

    # Wait for a short time to let settings stabilize
    sleep(0.5)

    # Take dummy capture to discard the first few frames
    picam2.capture_file("null.jpg")  # Discarded capture to ensure settings take effect

    # Wait for an additional short period to ensure settings have settled
    sleep(0.5)
    sleep(1*(frame_duration/1e6))

# Function to capture images with varying exposure times
def capture_images_with_varying_exposure(picam2):
    # Exposure times in microseconds
    exposure_times = [800000, 200000, 50000, 12500, 3125, 800, 400, 100, 50, 10]

    for i, exposure_time in enumerate(exposure_times):
        # Apply settings and wait for them to take effect
        apply_settings_and_discard_frames(picam2, exposure_time)

        # Capture the image
        filename = f'ldr_{i+1:02d}.jpg'
        picam2.capture_file(filename)
        print(f"Captured {filename} with exposure {exposure_time / 1e6:.6f} seconds")

        # Small delay between captures
        sleep(2 * (exposure_time / 1e6))

# Start camera
picam2.start()

# Capture the images
capture_images_with_varying_exposure(picam2)

# Stop the camera
picam2.stop()
