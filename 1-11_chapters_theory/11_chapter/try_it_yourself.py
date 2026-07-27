# 11.1, 11.2


def get_culture(city, country):
    """Returns a 'from' information."""
    formatted_culture = f"{city}, {country}"
    return (
        formatted_culture.title()
    )  #  pokracovanie v city_functions.py a test_cities.py


# 11.3
class Employee:
    """A simple testing employee class."""

    def __init__(self, first, last, salary):
        """Initializing classe's attributes."""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, amount=5000):
        """Raises annaul salary(default byt 5,000)"""
        self.salary += amount
