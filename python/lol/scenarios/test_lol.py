from pytest_bdd import scenario

# @scenario('./lol.feature', 'Visiting the Onezone as an anonymous user')
# def test_visit_onezone_anonymous():
#     pass

from lol.steps.lol import *
from pytest_bdd import scenarios
import pytest


@pytest.mark.nondestructive
@scenario('../features/lol.feature', 'Onezone page renders with proper title')
def test_onezone_page_renders_proper_title():
    pass


# assume 'features' subfolder is in this file's directory
scenarios('../features')

# @scenario('../features/lol.feature', 'Hello world')
# def test_hello_world():
#     pass
