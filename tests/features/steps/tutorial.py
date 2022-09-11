from behave import given, then, when


@given("we have behave installed")
def step_a(context):
    pass


@when("we implement a test")
def step_b(context):
    assert True is not False


@then("behave will test it for us!")
def step_c(context):
    assert context.failed is False
