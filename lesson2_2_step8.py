import os, time
from selenium import webdriver


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector('[name="firstname"]')
    first_name.send_keys("Default")
    first_name = browser.find_element_by_css_selector('[name="lastname"]')
    first_name.send_keys("Default")
    first_name = browser.find_element_by_css_selector('[name="email"]')
    first_name.send_keys("Default")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'upload.txt')
    upload_button = browser.find_element_by_id('file')
    upload_button.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

print(os.path.abspath(__file__))

print(os.path.abspath(os.path.dirname(__file__)))