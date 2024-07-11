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
            joints = body_frame.get_body_skeleton(body_id).joints

            # Do something with the joints data
            for joint in joints:
                print(f"Joint ID: {joint.id}, Position: {joint.position}, Orientation: {joint.orientation}")

    # Display the frame (optional)
    cv2.imshow('Depth Image', capture.get_colored_depth_image())

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
