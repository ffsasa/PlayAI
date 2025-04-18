import cv2
from hand_tracker.detector import HandDetector
from hand_tracker.gesture_controller import GestureController
from utils.timer import CooldownTimer

def main():
    # Khởi tạo các đối tượng cần thiết
    cap = cv2.VideoCapture(0)  # Mở webcam
    detector = HandDetector()  # Khởi tạo HandDetector
    controller = GestureController()  # Khởi tạo GestureController

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Phát hiện bàn tay và lấy danh sách các điểm landmark
        frame, landmarks_list = detector.detect(frame)

        # Kiểm tra nếu có ít nhất 1 bàn tay được phát hiện
        if landmarks_list:
            # Gọi phương thức detect_gesture để nhận diện cử chỉ và thực hiện hành động
            controller.detect_gesture(landmarks_list[0])

        # Hiển thị khung hình
        cv2.imshow("Hand Gesture Control", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
