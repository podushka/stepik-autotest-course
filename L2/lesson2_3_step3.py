from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_id('input_value').text)
    #y = int(browser.find_element_by_id('num2').text)
    button = browser.find_element_by_tag_name("button")
    
    
    
    #answer = browser.find_element_by_id('dropdown')
    #select = Select(answer)
    #select.select_by_visible_text(calc(x, y))
    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))

    robot_checkbox = browser.find_element_by_id('robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()
    robots_rule_radio = browser.find_element_by_id('robotsRule')
    robots_rule_radio.click()

    
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    # Отправляем заполненную форму
    
    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()