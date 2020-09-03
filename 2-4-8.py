from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(n):
    return str(math.log(abs(12*math.sin(int(n)))))

try:
    browser.get(link)
    button = browser.find_element_by_id("book")
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()

    x_value = int(browser.find_element_by_id('input_value').text)
    x = calc(x_value)

    browser.find_element_by_id('answer').send_keys(x)
    button = browser.find_element_by_id("solve").click()

finally:
    time.sleep(5)
    browser.quit()
