from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from xvfbwrapper import Xvfb
import pyscreenshot as ImageGrab

# Screenshots:
# ---
# fullscreen
# im=ImageGrab.grab()
# im.show()
# ---
# part of the screen
# im=ImageGrab.grab(bbox=(10,10,500,500))
# im.show()
# ---
# to file
# ImageGrab.grab_to_file('im.png')

def test_hello():
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    # driver = webdriver.Opera({"browserName":"opera","chromeOptions":{"args":[],"extensions":[],"binary":"/usr/bin/opera"}})
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    # to file
    ImageGrab.grab_to_file('im.png')
    driver.close()


with Xvfb(width=1280, height=1024, colordepth=24) as xvfb:
    test_hello()
