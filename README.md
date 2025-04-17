hand_control_project/
│
├── main.py                   # Chạy chính (nơi bắt đầu)
├── requirements.txt          # Ghi lại thư viện cần cài
├── README.md                 # Ghi chú dự án, cách chạy
│
├── hand_tracker/             # Thư mục xử lý AI & camera
│   ├── __init__.py
│   ├── detector.py           # Xử lý phát hiện tay bằng MediaPipe
│   └── gesture_controller.py # Điều khiển dựa vào ngón tay
│
├── utils/
│   ├── __init__.py
│   └── timer.py              # Hàm chờ cooldown để tránh spam lệnh
│
└── assets/                   # Chứa icon, hình minh họa nếu cần sau này
