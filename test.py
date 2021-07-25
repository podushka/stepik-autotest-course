from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    # link1 = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #x_element = browser.find_element_by_id('input_value')
    #x = calc(x_element.text)
    x_element = browser.find_element_by_id('treasure')
    x = calc(x_element.get_attribute('valuex'))

    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(str(x))

    robot_checkbox = browser.find_element_by_id('robotCheckbox')
    robot_checkbox.click()

    robots_rule_radio = browser.find_element_by_id('robotsRule')
    robots_rule_radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()