import os, time, math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x = int(browser.find_element_by_id('input_value').text)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))

    buttonq = browser.find_element_by_css_selector("button.btn")
    buttonq.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

print(os.path.abspath(__file__))

print(os.path.abspath(os.path.dirname(__file__)))