from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

# Tạo ứng dụng Qt
app = QApplication([])

# Tạo cửa sổ chính
window = QMainWindow()
window.setWindowTitle('Ví dụ PyQt5')
window.setGeometry(100, 100, 400, 200)  # Thiết lập kích thước và vị trí của cửa sổ

# Tạo nhãn (label) và thêm vào cửa sổ
label = QLabel('Xin chào, PyQt5!', window)
label.move(20, 20)  # Thiết lập vị trí của nhãn trong cửa sổ

# Hiển thị cửa sổ
window.show()

# Chạy vòng lặp chính của ứng dụng
app.exec_()
