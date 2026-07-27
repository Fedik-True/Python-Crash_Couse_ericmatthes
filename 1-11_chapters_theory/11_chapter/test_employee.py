import pytest
from try_it_yourself import Employee


@pytest.fixture
def emp():
    """Creates employee instance"""
    emp = Employee("Frederik", "Kukuca", 20000)
    return emp


def test_give_default_raise(emp):
    """Tests the default raise of the salary."""
    emp.give_raise()
    assert emp.salary == 25000


def test_give_custom_raise(emp):
    """Tests custom raise of the salary."""
    emp.give_raise(10000)
    assert emp.salary == 30000
