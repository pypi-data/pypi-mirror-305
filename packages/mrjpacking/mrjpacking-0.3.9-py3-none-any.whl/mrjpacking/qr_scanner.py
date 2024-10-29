import cv2
from .constants import frame_width, frame_height, FRAME_COLOR

# Khởi tạo detector một lần
detector = cv2.QRCodeDetector()

def preprocess_frame(frame):
    """Tiền xử lý khung hình để tăng cường phát hiện mã QR."""
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Chuyển đổi sang thang độ xám
    blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)  # Làm mờ để giảm nhiễu
    return blurred_frame

def capture_label(frame):
    if frame is None or frame.size == 0:
        return None  # Trả về None nếu khung hình không hợp lệ

    processed_frame = preprocess_frame(frame)  # Tiền xử lý khung hình

    try:
        data, vertices, _ = detector.detectAndDecode(processed_frame)
        
        if vertices is not None and data:
            return data  # Trả về dữ liệu nếu mã QR hợp lệ
            
    except cv2.error:
        return None

    return None

def check_within_frame(vertices):
    vertices = vertices.astype(int)
    x, y, w, h = cv2.boundingRect(vertices)
    return x >= 0 and y >= 0 and (x + w) <= frame_width and (y + h) <= frame_height

def draw_green_frame_around_qr(frame):
    processed_frame = preprocess_frame(frame)  # Tiền xử lý khung hình

    try:
        data, points, _ = detector.detectAndDecode(processed_frame)

        if points is not None and data and cv2.contourArea(points) > 0:
            # Chuyển đổi tọa độ điểm về kiểu int
            points = points[0].astype(int)
            
            # Vẽ khung xanh quanh mã QR
            cv2.polylines(frame, [points], isClosed=True, color=FRAME_COLOR, thickness=2)

    except cv2.error:
        pass

    return frame

