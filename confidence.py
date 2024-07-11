import pykinect_azure as pykinect
import cv2

# Initialize the library
pykinect.initialize_libraries(track_body=True)

# Configure the device
device = pykinect.start_device()

while True:
    # Capture a frame
    capture = device.update()

    # Get body tracking results
    body_frame = capture.get_body_frame()

    if body_frame:
        # Get the number of bodies detected
        num_bodies = body_frame.get_num_bodies()

        for body_id in range(num_bodies):
            # Get the joints of the body
            skeleton = body_frame.get_body_skeleton(body_id)
            joints = skeleton.joints

            for joint in joints:
                # Access joint confidence
                confidence = joint.confidence
                position = joint.position
                print(f"Joint ID: {joint.id}, Confidence: {confidence}, Position: {position}")

                # Use the confidence score for your application logic
                if confidence > 0.5:  # Example threshold
                    # Process joint data
                    pass

    # Display the frame (optional)
    cv2.imshow('Depth Image', capture.get_colored_depth_image())

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
