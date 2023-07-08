import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, models

# Đường dẫn đến thư mục chứa tập dữ liệu ảnh bình nước
water_bottle_dir = r'D:\TDM University\HK3_Nam4\AI\MachineLearningMadeEasy_FEX\MachineLearningMadeEasy_FEX\CarFinder\trainingImages\binhnuoc1'

# Đường dẫn đến thư mục chứa tập dữ liệu ảnh không phải bình nước
non_water_bottle_dir = r'D:\TDM University\HK3_Nam4\AI\MachineLearningMadeEasy_FEX\MachineLearningMadeEasy_FEX\CarFinder\trainingImages\binhnuoc2'
image_height = 100
image_width = 100
# Hàm đọc và tiền xử lý ảnh


def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (image_height, image_width))
    image = image / 255.0  # Chuẩn hóa giá trị pixel về khoảng [0, 1]
    return image


# Đọc và tiền xử lý dữ liệu ảnh
images = []
labels = []

# Đọc ảnh bình nước
for image_name in os.listdir(water_bottle_dir):
    image_path = os.path.join(water_bottle_dir, image_name)
    if image_path.endswith('.jpg') or image_path.endswith('.png'):
        image = preprocess_image(image_path)
        images.append(image)
        labels.append(1)  # Gán nhãn 1 cho ảnh bình nước

# Đọc ảnh không phải bình nước
for image_name in os.listdir(non_water_bottle_dir):
    image_path = os.path.join(non_water_bottle_dir, image_name)
    if image_path.endswith('.jpg') or image_path.endswith('.png'):
        image = preprocess_image(image_path)
        images.append(image)
        labels.append(0)  # Gán nhãn 0 cho ảnh không phải bình nước

# Chuyển đổi danh sách thành mảng numpy
images = np.array(images)
labels = np.array(labels)

# Chia tập dữ liệu thành tập huấn luyện và tập kiểm tra
train_images, test_images, train_labels, test_labels = train_test_split(
    images, labels, test_size=0.2, random_state=42)

# Xác định kích thước ảnh đầu vào
image_height, image_width, num_channels = train_images[0].shape

# Xây dựng mô hình CNN
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(
        image_height, image_width, num_channels)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# Biên dịch mô hình
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Huấn luyện mô hình
model.fit(train_images, train_labels, epochs=10,
          validation_data=(test_images, test_labels))

# Lưu mô hình
model.save('water_bottle_model.h5')
