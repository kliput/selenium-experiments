from pytest_bdd import scenario, given, when, then

# @scenario('./lol.feature', 'Visiting the Onezone as an anonymous user')
# def test_visit_onezone_anonymous():
#     pass

from lol import Screenshot
from lol.steps.lol import *
from pytest_bdd import scenarios

# assume 'features' subfolder is in this file's directory
scenarios('../features')

# @scenario('../features/lol.feature', 'Onezone login page renders with proper title')
# def test_a():
#     pass

# @scenario('../features/lol.feature', 'Hello world')
# def test_hello_world():
#     pass