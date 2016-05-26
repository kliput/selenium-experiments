from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from xvfbwrapper import Xvfb
import pyscreenshot as ImageGrab

# monkey-patching Selenium WebDriver

def wd_enter(wd):
    return wd

def wd_exit(wd, exc_type, exc_val, exc_tb):
    print 'An error occured in test -> error.png'
    ImageGrab.grab_to_file('error.png')
    wd.close()

webdriver.remote.webdriver.WebDriver.__enter__ = wd_enter
webdriver.remote.webdriver.WebDriver.__exit__ = wd_exit

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
    with driver:
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        # raise 'bad'
        # to file
        ImageGrab.grab_to_file('end.png')


# with Xvfb(width=1280, height=1024, colordepth=24) as xvfb:
test_hello()
