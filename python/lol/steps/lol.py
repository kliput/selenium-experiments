from pytest_bdd import scenario, given, when, then, parsers


class Something:
    def __init__(self):
        self.some_val = 0

    def foo(self):
        self.some_val += 42


# @given("I'm visiting Onezone site")
# def visit_onezone():
#     print 'visiting onezone'
#
# @when('I go to the login page')
# def visit_login_page():
#     print 'visiting login page'
#
# @then(parsers.parse('I should see at least <btn_count> login buttons'))
# def find_n_login_buttons(num_of_login_buttons):
#     print 'should find {n} login buttons'.format(n=num_of_login_buttons)
#
# @then(parsers.parse('I should see a <provider_name> login button'))
# def find_n_login_buttons(provider_name):
#     # TODO
#     print 'should find {name} login buttons'.format(name=provider_name)

@given('I have some object')
def some_object():
    return Something()


@when('I invoke foo method <times> times')
def invoke_foo_n_times(some_object, times):
    for i in range(0, int(times)):
        some_object.foo()


@then('The some_val property of object should equal <value>')
def some_val_equals(some_object, value):
    assert some_object.some_val == int(value)