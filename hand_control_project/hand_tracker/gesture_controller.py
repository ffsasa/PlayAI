import pyautogui

class GestureController:
    def __init__(self):
        self.prev_y = None
        self.scroll_threshold = 30  # Độ dài vuốt tối thiểu
        self.state = "idle"         # Trạng thái: idle, scrolling_up, scrolling_down

    def detect_gesture(self, current_landmarks):
        if not current_landmarks:
            self.prev_y = None
            self.state = "idle"
            return

        index_tip = current_landmarks[8]
        curr_y = index_tip[1]

        if self.prev_y is None:
            self.prev_y = curr_y
            return

        dy = curr_y - self.prev_y

        if self.state == "idle":
            if dy < -self.scroll_threshold:
                print("Scroll down")
                pyautogui.scroll(-300)
                self.state = "scrolling_down"
            elif dy > self.scroll_threshold:
                print("Scroll up")
                pyautogui.scroll(300)
                self.state = "scrolling_up"

        elif self.state == "scrolling_down":
            # Chờ tay quay lại vị trí ban đầu (gần vị trí cũ)
            if dy > self.scroll_threshold / 2:
                self.state = "idle"

        elif self.state == "scrolling_up":
            if dy < -self.scroll_threshold / 2:
                self.state = "idle"

        self.prev_y = curr_y
