import unittest, time
from selenium import webdriver


class Test(unittest.TestCase):
    def test_register1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
        first_name.send_keys("Default")
        last_name = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
        last_name.send_keys("Default")
        email = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
        email.send_keys("Default")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_register2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
        first_name.send_keys("Default")
        last_name = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
        last_name.send_keys("Default")
        email = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
        email.send_keys("Default")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == '__main__':
    unittest.main()