from selenium import webdriver

def check_credentials():
    # Khởi tạo trình điều khiển trình duyệt (ví dụ: Chrome)
    driver = webdriver.Chrome()

    # Lặp qua các tài khoản từ teky0055 đến teky0150
    for i in range(55, 151):
        username = f"tekyvr{str(i).zfill(4)}"
        password = "teky@1234"

        # Mở trang đăng nhập
        driver.get("https://edu.cospaces.io/Auth")

        # Tìm phần tử input tên đăng nhập và nhập thông tin
        username_input = driver.find_element_by_id("Username")
        username_input.send_keys(username)

        # Tìm phần tử input mật khẩu và nhập thông tin
        password_input = driver.find_element_by_id("Password")
        password_input.send_keys(password)

        # Submit biểu mẫu để đăng nhập
        login_button = driver.find_element_by_id("login-button")
        login_button.click()

        # Đợi cho trang đăng nhập xử lý
        driver.implicitly_wait(10)

        # Kiểm tra xem có thông báo lỗi đăng nhập hay không
        error_message = driver.find_elements_by_class_name("error-message")
        if error_message:
            print(f"Tài khoản {username} không hợp lệ.")
        else:
            print(f"Tài khoản {username} có mật khẩu đúng.")

    # Đóng trình duyệt
    driver.quit()

# Sử dụng hàm để kiểm tra tài khoản và mật khẩu
check_credentials()
