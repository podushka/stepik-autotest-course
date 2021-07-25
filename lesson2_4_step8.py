import os, time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))

    button = browser.find_element_by_id('book')
    button.click()
    

    x = int(browser.find_element_by_id('input_value').text)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))

    buttonq = browser.find_element_by_id('solve')
    buttonq.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

print(os.path.abspath(__file__))

print(os.path.abspath(os.path.dirname(__file__)))