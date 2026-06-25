class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog("Sullivan", 6)
your_dog = Dog("Lucy", "3")

print(f"My dog/s name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.roll_over()


# Try it yourself
# 9.1,  9.2
class Restaurant:
    """Restaurant model"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant's basic informations."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        "Printing informations."
        print(
            f"The restaurant's name is {self.restaurant_name} and it's cuisine type is {self.cuisine_type}"
        )

    def open_restaurant(self):
        """Prints message indicating the restaurant is open."""
        print(f"The {self.restaurant_name} is OPEN!")


my_restaurant = Restaurant("Neapoli", "Italliano")
print(
    f"Restaurant's name is {my_restaurant.restaurant_name} and it's cuisine type is {my_restaurant.cuisine_type}"
)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


sec_restaurant = Restaurant("Alibaba", "Turkish")
third_restaurant = Restaurant("Meder", "Slovakish")

sec_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()


# 9.3
class User:
    """User model"""

    def __init__(self, first_name, last_name, age, country, languages):
        """User's information"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.languages = languages

    def describe_user(self):
        """Prints user's description"""
        print(
            f"USERS INFORMATION:\n\tFirst name: {self.first_name.title()}\n\tLast name: {self.last_name.title()}\n\tAge: {self.age}\n\tCountry: {self.country.title()}\n\tLanguages: {self.languages}\n"
        )

    def greet_user(self):
        """Personalized greeting the user"""
        print(f"Hi {self.first_name.title()}!\n")


frederik = User("frederik", "kukuca", 24, "slovakia", "python")
frederik.greet_user()
frederik.describe_user()
justina = User("justina", "kalamenova", 28, "slovakia", "english")
justina.greet_user()
justina.describe_user()
