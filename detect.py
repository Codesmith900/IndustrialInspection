import cv2
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# Function to process frame
def process_frame(frame, model):
    # Dummy implementation for demonstration
    return False

def inspect_conveyor_belt(video_source, model):
    if model is None:
        raise ValueError("Model is not provided.")

    # Open video capture
    cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        raise ValueError("Failed to open video capture.")

    while cap.isOpened():
        # Read a frame from the video source
        ret, frame = cap.read()

        if not ret:
            break

        # Process the frame
        defect_detected = process_frame(frame, model)

        # Display the result on the frame
        if defect_detected:
            cv2.putText(frame, 'Defect Detected', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, 'No Defect', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Convert frame to RGB (OpenCV uses BGR by default)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame using Matplotlib
        plt.imshow(frame_rgb)
        plt.axis('off')
        plt.show()

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video capture
    cap.release()
    cv2.destroyAllWindows()

# Assuming 'model' is defined elsewhere in your script
model = load_model(r"D:\IndustrialDetection\casting_data\model.h5")

# Specify the path to the video file
video_path = "path/to/video.mp4"  # Replace "path/to/video.mp4" with the actual path to your video file

# Start inspection
inspect_conveyor_belt(video_source=video_path, model=model)
