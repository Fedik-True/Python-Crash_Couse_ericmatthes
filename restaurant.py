# 9/10

class Restaurant:
    """Restaurant model"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant's basic informations."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        "Printing informations."
        print(
            f"The restaurant's name is {self.restaurant_name} and it's cuisine type is {self.cuisine_type}"
        )

    def open_restaurant(self):
        """Prints message indicating the restaurant is open."""
        print(f"The {self.restaurant_name} is OPEN!")

    def customers_served(self):
        """Shows a number of customers served."""
        print(f"We served {self.number_served} so far.")

    def set_number_served(self, number):
        """Setting the number of serv ed customers."""
        if number > self.number_served:
            self.number_served = number
        else:
            print("You can't lower the amount of customers served!")

    def increment_number_served(self, number):
        """Incrementing the number of served customers."""
        if number > 0:
            self.number_served += number
        else:
            print("You can't roll back the amount of served customers!")
