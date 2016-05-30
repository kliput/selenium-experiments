from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from xvfbwrapper import Xvfb
import pyscreenshot as ImageGrab
import random

# monkey-patching Selenium WebDriver

def wd_enter(wd):
    return wd

def wd_exit(wd, exc_type, exc_val, exc_tb):
    try:
        screenshot_filename = 'error' + str(random.randint(1000, 9999)) + '.png'
        print 'An error occured in test -> {fn}'.format({
            'fn': screenshot_filename
        })
        ImageGrab.grab_to_file(screenshot_filename)
        wd.close()
    finally:
        return False

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
    # driver = webdriver.Firefox()

    # --no-sandbox option is needed to run Chrome with Selenium in Docker
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # driver = webdriver.Opera({"browserName":"opera","chromeOptions":{"args":[],"extensions":[],"binary":"/usr/bin/opera"}})

    with driver:
        driver.set_window_size(1280, 1024)
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        # raise 'bad'
        # to file
        screenshot_filename = 'end' + str(random.randint(1000, 9999)) + '.png'
        print 'end screenshot ->', screenshot_filename
        ImageGrab.grab_to_file(screenshot_filename)


# with Xvfb(width=1280, height=1024, colordepth=24) as xvfb:
test_hello()
