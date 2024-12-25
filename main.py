import cv2
import pygame
from gesture_utils import initialize_hands, identify_gesture

# Initialize Mediapipe Hand module
hands = initialize_hands()

# Initialize Pygame Mixer for music
pygame.mixer.init()
pygame.mixer.music.load('your_music_file.mp3')  # Replace with your music file

# Define gesture functions
def play_music():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def volume_up():
    pygame.mixer.music.set_volume(min(pygame.mixer.music.get_volume() + 0.1, 1.0))

def volume_down():
    pygame.mixer.music.set_volume(max(pygame.mixer.music.get_volume() - 0.1, 0.0))

# Gesture mapping (example gestures)
GESTURES = {
    '1': play_music,
    '2': stop_music,
    '3': volume_up,
    '4': volume_down
}

# Start webcam capture
cap = cv2.VideoCapture(0)

try:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Flip the frame horizontally and convert color space
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame for hand landmarks
        result = hands.process(frame_rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                gesture = identify_gesture(hand_landmarks)

                if gesture in GESTURES:
                    GESTURES[gesture]()

        # Display the frame
        cv2.imshow('Hand Gesture Music Player', frame)

        # Break loop on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    hands.close()
    pygame.mixer.quit()
