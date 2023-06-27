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

# làm mờ ảnh
# blur_image = cv2.GaussianBlur(image_resize, (5, 5), 2)

# hiển thị ảnh
# ảnh gốc
cv2.imshow('image', image_resize)

# ảnh làm mờ
# cv2.imshow('image_blur', blur_image)

# ảnh tăng độ sáng
cv2.imshow('equalized_image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
