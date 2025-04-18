# Import thư viện OpenCV và MediaPipe
import cv2                         # Thư viện xử lý ảnh, video (hiển thị webcam)
import mediapipe as mp             # Thư viện nhận diện tay, mặt, pose, v.v. theo thời gian thực của camera



# Tạo một lớp để phát hiện bàn tay
class HandDetector:
    # Hàm khởi tạo (constructor) của lớp
    def __init__(self, max_hands=1, detection_confidence=0.7):
        self.max_hands = max_hands                      # Số lượng tay tối đa cần phát hiện
        self.mp_hands = mp.solutions.hands              # Dùng mô-đun "hands" của MediaPipe

        # Khởi tạo đối tượng nhận diện tay
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,                    # False: dùng cho video (nhiều frame)
            max_num_hands=max_hands,                    # Số lượng tay tối đa cần tìm
            min_detection_confidence=detection_confidence  # Ngưỡng độ tin cậy khi phát hiện
        )

        self.mp_draw = mp.solutions.drawing_utils       # Công cụ để vẽ khung xương tay

        # Hàm detect: phát hiện tay trong 1 khung hình (frame) truyền vào
    def detect(self, frame):
        # Chuyển đổi ảnh từ BGR (mặc định OpenCV) sang RGB (cần cho MediaPipe)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Gửi ảnh vào MediaPipe để xử lý và tìm tay
        results = self.hands.process(rgb_frame)

        # Khởi tạo danh sách chứa các tọa độ điểm trên tay
        landmarks_list = []

                # Nếu có ít nhất 1 bàn tay được tìm thấy
        if results.multi_hand_landmarks:
            # Duyệt qua từng bàn tay được tìm thấy
            for handLms in results.multi_hand_landmarks:
                # Vẽ khung xương tay lên khung hình
                self.mp_draw.draw_landmarks(frame, handLms, self.mp_hands.HAND_CONNECTIONS)

                # Tạo danh sách để lưu tọa độ các điểm trên tay
                landmarks = []

                # Duyệt qua từng điểm (landmark) trên tay
                for lm in handLms.landmark:
                    h, w, c = frame.shape    # Lấy kích thước ảnh: height, width, channel

                    # Tính tọa độ (x, y) trên ảnh thật (vì lm.x và lm.y là tỉ lệ)
                    x = int(lm.x * w)
                    y = int(lm.y * h)

                    # Thêm tọa độ điểm vào danh sách
                    landmarks.append((x, y))

                # Thêm danh sách các điểm của 1 tay vào danh sách chung
                landmarks_list.append(landmarks)

        # Trả về khung hình (có vẽ tay) và danh sách các điểm trên tay
        return frame, landmarks_list

