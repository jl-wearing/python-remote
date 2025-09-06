import pytest
from employee import Employee

@pytest.fixture
def new_employee():
    """An employee that will be available to all test functions."""
    return Employee('lionel', 'messi', 1_000.00)

def test_give_default(new_employee):
    """Does giving an employee the default raise $5000 work?"""
    # Give the employee a raise.
    new_employee.give_raise()
    assert new_employee.annual_salary == 6000.00

def test_give_raise_125000(new_employee):
    """Does giving the employee a raise of $125000 work?"""

    new_employee.give_raise(125_000.00)
    assert new_employee.annual_salary == 126_000.00

def test_give_negative_raise(new_employee):
    """Does giving the employee a raise of $5000 work?"""
    new_employee.give_raise(-5000.00)
    assert new_employee.annual_salary == 1000.00