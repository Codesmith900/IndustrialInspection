import cv2
from tensorflow.keras.models import load_model
import tkinter as tk
from threading import Thread

# Dummy function for frame processing
def process_frame(frame, model):
    # Placeholder for actual defect detection logic
    return False

def inspect_conveyor_belt(video_source, model):
    cap = cv2.VideoCapture(video_source)
    
    def video_loop():
        while running:
            ret, frame = cap.read()
            if not ret:
                break

            defect_detected = process_frame(frame, model)
            if defect_detected:
                cv2.putText(frame, 'Defect Detected', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            else:
                cv2.putText(frame, 'No Defect', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.imshow('Conveyor Belt Inspection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    video_thread = Thread(target=video_loop)
    video_thread.start()

def stop_video():
    global running
    running = False
    root.quit()

# Load the model
model = load_model(r"D:\IndustrialDetection\casting_data\model.h5")

# Create a Tkinter window
root = tk.Tk()
root.title("Real-Time Conveyor Belt Inspection")

# Add a stop button to the window
stop_button = tk.Button(root, text="Stop", command=stop_video)
stop_button.pack()

# Set the running flag
running = True

# Start the video inspection
inspect_conveyor_belt(0, model)

# Run the Tkinter main loop
root.mainloop()
