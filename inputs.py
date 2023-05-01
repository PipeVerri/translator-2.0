import cv2
import mediapipe as mp

def get_landmarks(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5):
    cap = cv2.VideoCapture(0)
    mp_hands = mp.solutions.hands
    with mp_hands.Hands(static_image_mode=static_image_mode, max_num_hands=max_num_hands, min_detection_confidence=min_detection_confidence) as hands:
        while True:
            ret, frame = cap.read()
            if not ret:
                yield None

            frame_new = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_new)

            if results.multi_handedness is None:
                yield None

            yield results.multi_hand_landmarks
