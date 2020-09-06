import unittest
from selenium import webdriver
import time

def test_link(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_css_selector('.first_block .first').send_keys('Vasya')
    browser.find_element_by_css_selector('.first_block .second').send_keys('Pupkin')
    browser.find_element_by_css_selector('.first_block .third').send_keys('VasyaPupkin@mail.com')

    # Отправляем заполненную форму
    browser.find_element_by_css_selector("button.btn").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    return browser.find_element_by_tag_name("h1").text
    

class TestLink(unittest.TestCase):
    def test_link1(self):
        self.assertEqual(test_link("http://suninjuly.github.io/registration1.html"), "Congratulations! You have successfully registered!", 'welcome text isn\'t match')

    def test_link2(self):
        self.assertEqual(test_link("http://suninjuly.github.io/registration2.html"), "Congratulations! You have successfully registered!", 'welcome text isn\'t match')
        
if __name__ == "__main__":
    unittest.main()