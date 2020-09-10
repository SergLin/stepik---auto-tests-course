import time
import math
import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.mark.parametrize('link', links)
def test_set_correct_answer(browser, link):
    browser.get(link)
    browser.find_element_by_css_selector(".textarea").send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_css_selector('.submit-submission').click()
    assert browser.find_element_by_css_selector('.smart-hints__hint').text == 'Correct!', 'message is not "Correct!"'
