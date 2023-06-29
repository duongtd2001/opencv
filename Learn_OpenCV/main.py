import cv2
import numpy as np

path = r'D:\Python\opencv\Image_ssd.bmp'
image = cv2.imread(path)
image_resize = cv2.resize(image, (1280, 720))

# chuyển ảnh sang màu gray
gray_image = cv2.cvtColor(image_resize, cv2.COLOR_RGB2GRAY)

# điều chỉnh độ sáng
bringhtness = 20
bringhtness_image = np.clip(
    gray_image + bringhtness, 0, 255).astype(np.uint8)

# điều chỉnh độ tương phản
contrast = 1.2
bringhtness_image = np.clip(
    contrast * (gray_image - 128) + 128, 0, 255).astype(np.uint8)

# cân bằng màu sắc
equalized_image = cv2.equalizeHist(gray_image)


# tạo ma trận xoay ảnh
center = (gray_image.shape[1]//2, gray_image.shape[0]//2)
angle = 180
scale = 1.0
rotation = cv2.getRotationMatrix2D(center, angle, scale)
rotation_image = cv2.warpAffine(
    gray_image, rotation, (gray_image.shape[1], gray_image.shape[0]))


# áp dụng ngưỡng
_, thresholed_image = cv2.threshold(gray_image, 70, 255, cv2.THRESH_BINARY)

# làm mờ ảnh
blur_image = cv2.GaussianBlur(thresholed_image, (3, 3), 0)
# phát hiện biên với Canny
canny_image = cv2.Canny(blur_image, 50, 70)

# phát hiện biên với Sobel
'''gradient_x = cv2.Sobel(blur_image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(blur_image, cv2.CV_64F, 0, 1, ksize=3)

gradient_magnitude = cv2.magnitude(gradient_x, gradient_y)
threshold = 120
edges = cv2.threshold(gradient_magnitude, threshold, 255, cv2.THRESH_BINARY)[1]'''

# hiển thị ảnh
# ảnh gốc
cv2.imshow('image', image_resize)

# ảnh làm mờ
cv2.imshow('image_blur', blur_image)

# ảnh tăng độ sáng
cv2.imshow('canny_image', canny_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
