import k4a
import cv2
import numpy as np

# Initialize the Kinect device
device = k4a.Device.open()

# Configure the device
device.start_cameras(
    config={
        "color_format": k4a.K4A_IMAGE_FORMAT_COLOR_BGRA32,
        "color_resolution": k4a.K4A_COLOR_RESOLUTION_1080P,
        "depth_mode": k4a.K4A_DEPTH_MODE_NFOV_UNBINNED,
        "synchronized_images_only": True,
    }
)

# Initialize body tracker
tracker = k4a.Tracker.create()

while True:
    # Capture a frame
    capture = device.get_capture()

    # Update the tracker with the captured frame
    tracker.enqueue_capture(capture)

    # Get body tracking results
    frame = tracker.pop_result()

    if frame:
        bodies = frame.get_bodies()

        for body in bodies:
            skeleton = body.skeleton

            for joint in skeleton.joints:
                # Access joint confidence and position
                confidence = joint.confidence_level
                position = joint.position
                print(f"Joint ID: {joint.id}, Confidence: {confidence}, Position: {position}")

                # Use the confidence score for your application logic
                if confidence > k4a.K4A_CONFIDENCE_LEVEL_MEDIUM:  # Example threshold
                    # Process joint data
                    pass

    # Display the frame (optional)
    color_image = capture.color
    if color_image is not None:
        color_image = np.array(color_image, copy=False)
        cv2.imshow('Color Image', color_image)

    if cv2.waitKey(1) == 27:
        break

# Clean up
tracker.destroy()
device.stop_cameras()
cv2.destroyAllWindows()
