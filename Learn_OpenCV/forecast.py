import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Đường dẫn đến file water_bottle_model.h5
model_path = r'D:\Python\opencv\Learn_OpenCV\water_bottle_model.h5'

# Kích thước ảnh đầu vào
image_height = 100
image_width = 100

# Hàm đọc và tiền xử lý ảnh


def preprocess_image(image):
    image = cv2.resize(image, (image_height, image_width))
    image = image / 255.0  # Chuẩn hóa giá trị pixel về khoảng [0, 1]
    return image


# Load mô hình từ file
model = load_model(model_path)

# Khởi tạo camera
# Số 0 để chọn camera mặc định, nếu có nhiều camera thì có thể thay đổi số này
camera = cv2.VideoCapture(0)

while True:
    # Đọc khung hình từ camera
    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)
    # Tiền xử lý khung hình
    preprocessed_frame = preprocess_image(frame)

    # Mở rộng kích thước của khung hình để phù hợp với mô hình
    preprocessed_frame = np.expand_dims(preprocessed_frame, axis=0)

    # Dự đoán nhãn của khung hình
    prediction = model.predict(preprocessed_frame)

    # Chuyển đổi dự đoán thành nhãn
    if prediction[0][0] >= 0.8:
        label = "Bình nước"
    else:
        label = "Không phải bình nước"

    # Hiển thị nhãn lên khung hình
    cv2.putText(frame, label, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Hiển thị khung hình
    cv2.imshow("Camera", frame)

    # Nhấn phím 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng camera và đóng cửa sổ hiển thị
camera.release()
cv2.destroyAllWindows()
