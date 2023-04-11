import mediapipe as mp
import cv2

mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)

with mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5) as hands:
    while True:
        ret, frame = cap.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)

        if results.multi_handedness is not None:
            print(results.multi_handedness[0])

        cv2.imshow("frame", frame)
        cv2.waitKey(1)