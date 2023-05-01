import cv2
import mediapipe as mp


def read_image(path=None, cap_n=0):
    if path is None:
        while True:
            cap = cv2.VideoCapture(cap_n)
            _, frame = cap.read()
            frame_new = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            yield frame_new
    else:
        return cv2.imread(path)


def get_landmarks(img, static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5):
    mp_hands = mp.solutions.hands
    with mp_hands.Hands(static_image_mode=static_image_mode, max_num_hands=max_num_hands,
                        min_detection_confidence=min_detection_confidence) as hands:
        while True:
            results = hands.process(img)

            if results.multi_handedness is None:
                return None

            return results.multi_hand_landmarks
