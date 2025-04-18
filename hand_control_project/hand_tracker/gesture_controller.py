import pyautogui
import time
import math

class GestureController:
    def __init__(self):
        self.prev_y = None
        self.scroll_threshold = 30
        self.state = "idle"
        self.last_scroll_time = 0
        self.cooldown = 0.5

    def is_index_finger_straight(self, landmarks):
        # Kiểm tra ngón trỏ có duỗi thẳng không: điểm 6 -> 7 -> 8 gần thẳng hàng
        x6, y6 = landmarks[6]
        x7, y7 = landmarks[7]
        x8, y8 = landmarks[8]

        # Vector từ khớp 6->7 và 7->8
        v1 = (x7 - x6, y7 - y6)
        v2 = (x8 - x7, y8 - y7)

        # Tính cosine của góc giữa 2 vector
        def dot(v1, v2):
            return v1[0]*v2[0] + v1[1]*v2[1]
        def mag(v):
            return math.sqrt(v[0]**2 + v[1]**2)

        cos_angle = dot(v1, v2) / (mag(v1) * mag(v2) + 1e-6)
        angle = math.acos(cos_angle) * 180 / math.pi

        return angle < 20  # Nếu góc nhỏ thì ngón gần như thẳng

    def detect_gesture(self, current_landmarks):
        if not current_landmarks or not self.is_index_finger_straight(current_landmarks):
            self.prev_y = None
            self.state = "idle"
            return

        index_tip = current_landmarks[8]
        curr_y = index_tip[1]

        if self.prev_y is None:
            self.prev_y = curr_y
            return

        dy = curr_y - self.prev_y
        now = time.time()

        if self.state == "idle":
            if dy < -self.scroll_threshold and now - self.last_scroll_time > self.cooldown:
                print("Scroll down")
                pyautogui.scroll(-300)
                self.last_scroll_time = now
                self.state = "scrolling_down"

            elif dy > self.scroll_threshold and now - self.last_scroll_time > self.cooldown:
                print("Scroll up")
                pyautogui.scroll(300)
                self.last_scroll_time = now
                self.state = "scrolling_up"

        elif self.state in ("scrolling_up", "scrolling_down"):
            if abs(dy) < 5:
                self.state = "idle"

        self.prev_y = curr_y
