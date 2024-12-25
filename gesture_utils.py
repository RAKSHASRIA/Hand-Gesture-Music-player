import mediapipe as mp

# Initialize Mediapipe Hand module
mp_hands = mp.solutions.hands

def initialize_hands():
    """Initialize and return Mediapipe Hands solution."""
    return mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

def identify_gesture(hand_landmarks):
    """Identify gestures based on hand landmarks."""
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
    wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

    # Gesture for '1': index finger extended, others down
    if index_tip.y < wrist.y and middle_tip.y > wrist.y and ring_tip.y > wrist.y and pinky_tip.y > wrist.y:
        return '1'
    # Gesture for '2': index and middle fingers extended, others down
    elif index_tip.y < wrist.y and middle_tip.y < wrist.y and ring_tip.y > wrist.y and pinky_tip.y > wrist.y:
        return '2'
    # Gesture for '3': index, middle, and ring fingers extended, pinky down
    elif index_tip.y < wrist.y and middle_tip.y < wrist.y and ring_tip.y < wrist.y and pinky_tip.y > wrist.y:
        return '3'
    # Gesture for '4': all fingers extended
    elif index_tip.y < wrist.y and middle_tip.y < wrist.y and ring_tip.y < wrist.y and pinky_tip.y < wrist.y:
        return '4'
    return None
