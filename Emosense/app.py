import cv2
from deepface import DeepFace

# Load the face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def start_app():
    # Open the webcam
    cap = cv2.VideoCapture(0)
    
    print("Starting EmoSense Desktop App...")
    print("Press 'q' on your keyboard to stop.")

    frame_counter = 0
    current_emotion = "Scanning..."

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 1. Optimize: Only analyze emotion every 10 frames to stop lag
        frame_counter += 1
        if frame_counter % 10 == 0:
            try:
                # Analyze the frame
                result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                current_emotion = result[0]['dominant_emotion']
                print(f"Emotion detected: {current_emotion}") # Prints inside VS Code terminal
            except:
                pass

        # 2. Draw the Emotion Text on the video
        cv2.rectangle(frame, (0,0), (640, 60), (0,0,0), -1) # Black banner at top
        cv2.putText(frame, f"Emotion: {current_emotion.upper()}", (20, 40), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # 3. Show the window directly (No Browser needed!)
        cv2.imshow('EmoSense - VS Code Python', frame)

        # 4. Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_app()