import cv2
import mediapipe as mp


class HandDetector:
    def __init__(self, max_hands=1, detection_confidence=0.7):
        self.max_hands = max_hands
        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_hands,
            min_detection_confidence=detection_confidence
        )

        self.mp_draw = mp.solutions.drawing_utils

    def detect(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        landmarks_list = []

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, handLms, self.mp_hands.HAND_CONNECTIONS)

                landmarks = []
                h, w, _ = frame.shape

                for lm in handLms.landmark:
                    x = int(lm.x * w)
                    y = int(lm.y * h)
                    landmarks.append((x, y))

                # Chỉ thêm nếu có đủ số lượng landmark
                if len(landmarks) >= 21:
                    landmarks_list.append(landmarks)

        return frame, landmarks_list
