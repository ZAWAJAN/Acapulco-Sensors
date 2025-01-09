from picamera2 import Picamera2, Preview
import libcamera
from time import sleep

# Initialize the camera
picam2 = Picamera2()

# Configure initial camera settings
camera_config = picam2.create_still_configuration(
    controls={
        "AwbEnable": False,
        "AwbMode": libcamera.controls.AwbModeEnum.Daylight,
        "ExposureTime": 1000,
        "AnalogueGain": 1.0  # equivalent to a ISO 100
    }
)
picam2.configure(camera_config)
#print(picam2.capture_metadata())

# Function to capture images with varying exposure times
def capture_images_with_varying_exposure(picam2):
    # Exposure times in microseconds
    # exposure_times = [800000, 200000, 50000, 12500, 3125, 800, 400, 100, 50, 10]
    exposure_times = [4000000, 2000000, 500000, 125000, 31250, 8000, 2000, 500, 125]

    for i, exposure_time in enumerate(exposure_times):
        # Apply settings and wait for them to take effect
        #apply_settings_and_discard_frames(picam2, exposure_time)
        frame_duration = int(exposure_time * 1.25)
        picam2.set_controls({"ExposureTime": exposure_time,
                             "FrameDurationLimits": (frame_duration, frame_duration),
                             "AnalogueGain": 1.0})

        # Capture the image
        picam2.start()
        filename = f'ldr_{i+1:02d}.jpg'
        picam2.capture_file(filename)
        print(picam2.capture_metadata())
        print(f"Captured {filename} with shutter speed {exposure_time / 1e6:.6f} seconds\n")

        # Small delay between captures
        #sleep(2 * (exposure_time / 1e6))
        sleep(1)
        picam2.stop()


# Capture the images
capture_images_with_varying_exposure(picam2)

