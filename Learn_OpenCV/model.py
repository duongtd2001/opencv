import cv2
import numpy as np

# Đọc ảnh chứa bảng mạch
image = cv2.imread(r'D:\Python\opencv\cpuNG.jpg')
image = cv2.resize(image, (640, 480))
# Tiền xử lý ảnh
threshold_width = 100
threshold_height = 100
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
edges = cv2.Canny(blurred_image, 50, 150)

# Phát hiện vùng chứa linh kiện
contours, _ = cv2.findContours(
    edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Duyệt qua các vùng chứa linh kiện
for contour in contours:
    # Lấy hình chữ nhật bao quanh vùng chứa linh kiện
    x, y, w, h = cv2.boundingRect(contour)

    # Kiểm tra điều kiện linh kiện thiếu/lỗi lắp ráp
    if w < threshold_width or h < threshold_height:
        # Đánh dấu linh kiện thiếu/lỗi lắp ráp
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

# Hiển thị ảnh kết quả
cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
