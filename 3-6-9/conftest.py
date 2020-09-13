import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb', help='select language')


@pytest.fixture(scope='function')
def browser():
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope='function')
def lang(request):
    lang = request.config.getoption('language')
    yield lang
