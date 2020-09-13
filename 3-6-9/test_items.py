import time

def test_basket_button_available(browser, lang):
    browser.get(f'http://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/')
    time.sleep(30)
    assert browser.find_element_by_css_selector('.btn-add-to-baskets'), "The 'basket' button isn't displayed"
