from pytest_bdd import given, when, then, parsers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re


class Something:
    def __init__(self):
        self.some_val = 0

    def foo(self):
        self.some_val += 42


@given("I'm visiting Onezone site")
def visit_onezone(base_url, selenium):
    # TODO: configure address of OZ
    oz_url = base_url
    selenium.get(oz_url)


@when('I go to the <page> page')
@when(parsers.re(r'I go to the (?P<page>.+) page'))
def visit_login_page(selenium, page):
    selenium.get(selenium.current_url + '#' + page)


@then('The page title should contain <title>')
@then('The page title should contain {title}')
def title_matches(selenium, title):
    assert re.match(r'.*' + title + r'.*', selenium.title, re.IGNORECASE)


@then(parsers.parse('I should see at least {btn_count:d} login buttons'))
def find_n_login_buttons(selenium, btn_count):
    assert len(selenium.find_elements_by_css_selector('a.login-icon-box')) >= btn_count


@then(parsers.parse('I should see a <provider_name> login button'))
def find_provider_button(selenium, provider_name):
    ## TODO: explicit wait
    # assert WebDriverWait(selenium, 5).until(
    #     EC.element_to_be_clickable(By.css_selector(
    #         'a.login-icon-box.{name}'.format(name=provider_name)
    #     ))
    # )
    selenium.implicitly_wait(5)
    assert selenium.find_element_by_css_selector(
        'a.login-icon-box.{name}'.format(name=provider_name)
    )
