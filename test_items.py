import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_but_bascket(browser):
    browser.get(link)
    time.sleep(30)
    but = browser.find_element_by_css_selector("button[type='submit']")
    assert but, "Button error"
