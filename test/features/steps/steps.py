from behave import *

from app import Calculator


@given('a {values} to sum')
def step_impl(context, values):
    context.calculator = Calculator()
    context.values = values.split(',')

@when('the calculator sums the values')
def step_impl(context):
    context.total = context.calculator.add(int(context.values[0]),int(context.values[1]))

@then('the {total:d} of sum is correct')
def step_impl(context, total):
    assert (context.total == total)

@given('a {values} to substract')
def step_impl(context, values):
    context.calculator = Calculator()
    context.values = values.split(',')

@when('the calculator substract the values')
def step_impl(context):
    context.total = context.calculator.subtract(int(context.values[0]),int(context.values[1]))

@then('the {total:d} of substraction is correct')
def step_impl(context, total):
    assert (context.total == total)


@given('a {values} to multiply')
def step_impl(context, values):
    context.calculator = Calculator()
    context.values = values.split(',')

@when('the calculator multiply the values')
def step_impl(context):
    context.total = context.calculator.multiply(int(context.values[0]),int(context.values[1]))

@then('the {total:d} of multiply is correct')
def step_impl(context, total):
    assert (context.total == total)