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
# 9.1,  9.2, 9.4
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


restaurant = Restaurant("krcma pod lipou", "slovakian")
restaurant.customers_served()
restaurant.set_number_served(10)
restaurant.customers_served()
restaurant.increment_number_served(142)
restaurant.customers_served()


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


# 9.3, 9.5
class User:
    """User model"""

    def __init__(self, first_name, last_name, age, country, languages):
        """User's information."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.languages = languages
        self.login_attempts = 0

    def describe_user(self):
        """Prints user's description."""
        print(
            f"USERS INFORMATION:\n\tFirst name: {self.first_name.title()}\n\tLast name: {self.last_name.title()}\n\tAge: {self.age}\n\tCountry: {self.country.title()}\n\tLanguages: {self.languages}\n"
        )

    def greet_user(self):
        """Personalized greeting the user."""
        print(f"Hi {self.first_name.title()}!\n")

    def increment_login_attempts(self):
        """Counting login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reseting login attempts count to zero."""
        self.login_attempts = 0


frederik = User("frederik", "kukuca", 24, "slovakia", "python")
frederik.greet_user()
frederik.describe_user()
justina = User("justina", "kalamenova", 28, "slovakia", "english")
justina.greet_user()
justina.describe_user()
frederik.increment_login_attempts()
frederik.increment_login_attempts()
frederik.increment_login_attempts()
print(frederik.login_attempts)
frederik.reset_login_attempts()
print(frederik.login_attempts)


# car
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")


# my_used_car = Car("subaru", "outback", 2019)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()


# ====
# COMPOSITION
# ===


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the  battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go  ab out {range} miles on a full charge.")

    def upgrade_battery(self):
        """Changing the battery size to 65 kWh"""
        if self.battery_size == 65:
            print(f"Battery's up to date.")
        else:
                self.battery_size = 65



# ====
# INHERITANCE
# ===

# 9.9 Battery upgrade
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.fill_gas_tank()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()

# Try it yourself
# 9.6 Ice cream Stand
class Ice_cream_stand(Restaurant):
    """A simple subclass(child) of the Restaurant superclass."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant's properties."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['lemon', 'chocolate', 'vanilla']

    def display_flavors(self):
        """Show flavors."""
        print(f"Our ice-cream flavor's are:\n{"\n".join(self.flavors)}")


zmrzka = Ice_cream_stand("Zmrrrrzka", "zmrzlinaren")
zmrzka.display_flavors()


# 9.8 Privileges
class Privileges:
    """Simple privileges model."""

    def __init__(self):
        """Initialize privileges."""
        self.privileges = ['can add post', 'can delete post', 'can bar user']

    def show_privileges(self):
        """Shows all the privileges admin has."""
        print(f"Admin's privileges:\n\t{'\n\t'.join(self.privileges)}")


# 9.7 Admin

class Admin(User):
    """Simple subclass of User superclass."""

    def __init__(self, first_name, last_name, age, country, languages):
        """Initialize admin's properties."""
        super().__init__(first_name, last_name, age, country, languages)
        self.privileges = Privileges()



admin = Admin('Frederik', 'Kukuca', 24, 'Slovakia', 'english, slovakian')
admin.privileges.show_privileges()


# from random import randint
# randint(1,6)

# from random import choice
# players =['charles', 'martina', 'michael', 'florence', 'eli']
# first_up = choice(players)
# first_up



# Try it youself
# 9.13
from email.errors import InvalidMultipartContentTransferEncodingDefect
from random import randint
from random import choice
import random

class Die:
    """A simple model of a playing die."""

    def __init__(self, sides=6):
        """Initialize die's properties."""
        self.sides = sides

    def roll_dice(self):
        """Simulating a roll."""
        for roll in range(3):
            print("ROLLING....")

        number = randint(1, self.sides)
        print(f"You rolled a {number}!")


dnd_die = Die(6)
dnd_die.roll_dice()
dnd_die.sides=10
dnd_die.roll_dice()
dnd_die.sides=20
dnd_die.roll_dice()


# 9.14, 9.15
counter = 0
while True:

    characters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

    my_ticket = []
    random_items = []

    for char in range(4):
        item = choice(characters)
        random_items.append(item)

    for char in range(4):
        item = choice(characters)
        my_ticket.append(item)

    print("The prize goes to a whoever has these characters:")

    for char in random_items:
        print(char," ", end="")
    print()
    for char in my_ticket:
        print(char," ", end="")

    if my_ticket == random_items:
        print("CONGRATULATIONS!\nYou won!")
        print(f"With total counts of {counter}!")
        break
    else:
        counter += 1
        continue

#----------------
# DOPILOVANIE OOP
#----------------


class Dog:
    """Defining a dog class."""

    def __init__(self, name, breed):
        """Initializing dog's attributes."""
        self.name = name
        self.breed = breed

    def introduce(self):
        """Introducing the dog."""
        print(f"Hi! My  name is {self.name.title()}, i am {self.breed}.")


aya = Dog("aya", "jag-terrier")
aya.introduce()





class BankAccount:
    """A simple bank account model."""

    def __init__(self, owner, balance=0):
        """Initializing bank account's attributes."""
        self.owner = owner
        self.balance =  balance

    def deposit(self, number):
        """Adds funds to balance."""
        self.balance += number

    def withdraw(self, number):
        """Subtracts a number from the balance."""
        if number <= self.balance:
            self.balance -= number
        else:
            print("Insufficient funds.")





class Counter:
    """A simple counter model."""

    def __init__(self, count=0):
        """Initializing an counter attributes."""
        self.count = count

    def increment(self, number):
        """Adding to counter."""
        if number > 0:
            self.count += number
        else:
            print("Number must be greater than 0.")

    def decrement(self, number):
        """Subtracts a number from the counter."""
        if number < self.count:
            self.count -= number
        else:
            print("Insufficient number.")

    def reset(self):
        """Reseting the counter."""
        self.count = 0

    def show(self):
        """Printing the value of the counter."""
        print(f"Actual value of counter is {self.count}.")

shower = Counter()
shower.increment(5)
shower.show()
shower.decrement(3)
shower.show()
shower.reset()
shower.show()





class Student:
    """A simple student model."""

    def __init__(self,  name, age, grades=[]):
        """Initializing student attributes."""
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade):
        """Adding a grade."""
        self.grades.append(grade)

    def average_grade(self):
        """Printing an average grade."""
        print(f"{self.name}'s average grade is {int(sum(self.grades) / len(self.grades))}.")

    def show_info(self):
        """Printing student's details."""
        print(f"Name: {self.name}\nAge: {self.age}\nAverage grade: {int(sum(self.grades) / len(self.grades))}")

frederik = Student("Frederik", 24)
frederik.add_grade(5)
frederik.add_grade(3)
frederik.add_grade(2)
frederik.add_grade(2)
frederik.average_grade()
frederik.show_info()
print(frederik.grades)





class IceCreamShop:
    """A simple ice cream shop model."""

    def __init__(self, flavors=[]):
        """Initializing shop's attributes."""
        self.flavors = flavors

    def add_flavor(self, flavor):
        """Adding a flavor."""
        self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        """Subtract a flavor."""
        self.flavors.remove(flavor)

    def show_flavors(self):
        """Prints a list of  flavors."""
        print("===Flavors===")
        print("-" * 13)
        for flavor in self.flavors:
            print(flavor)

jojo = IceCreamShop()
jojo.add_flavor("orange")
jojo.add_flavor("apple")
jojo.add_flavor("chocolate")
jojo.add_flavor("vanilla")
jojo.show_flavors()





class Rectangle:
    """A simple rectangle model."""

    def __init__(self, height, width):
        """Initializing a rectangle's attributes."""
        self.height = height
        self.width = width

    @property
    def area(self):
        """Defining an area of rectangle."""
        return self.height * self.width


objekt = Rectangle(5, 10)
print(objekt.area)
