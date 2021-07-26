import pytest, time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



full_text = ''

page_list = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('page', page_list)
def test_guest_should_see_login_link(browser, page):
    browser.get(page)
    textarea = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea')))
    answer = str(math.log(int(time.time())))
    textarea.send_keys(answer)
    button = browser.find_element_by_css_selector('button.submit-submission')
    button.click()
    text = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'pre.smart-hints__hint')))
    if text.text != 'Correct!':
        print("\n Текст: {}".format(text.text))
        full_text.join(text.text)
        print(full_text)
        raise AssertionError('Сообщение неверно!')



