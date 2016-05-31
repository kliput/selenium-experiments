from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from xvfbwrapper import Xvfb
import pyscreenshot as ImageGrab
import random

# monkey-patching Selenium WebDriver

def wd_enter(driver):
    return driver

def wd_exit(driver, exc_type, exc_val, exc_tb):
    try:
        screenshot_filename = 'error' + str(random.randint(1000, 9999)) + '.png'
        print 'An error occured in test -> {fn}'.format({
            'fn': screenshot_filename
        })
        driver.get_screenshot_as_file(driver)

        # ImageGrab.grab_to_file(screenshot_filename)
        driver.close()

    finally:
        raise Exception('lol')
        # return False

webdriver.remote.webdriver.WebDriver.__enter__ = wd_enter
webdriver.remote.webdriver.WebDriver.__exit__ = wd_exit


class Screenshot(object):

    def __init__(self, driver):
        self.driver = driver

    def __call__(self, original_func):
        decorator_self = self

        def wrappee(*args, **kwargs):
            try:
                original_func(*args,**kwargs)
            finally:
                decorator_self.driver.get_screenshot_as_file('test1.png')

        return wrappee
