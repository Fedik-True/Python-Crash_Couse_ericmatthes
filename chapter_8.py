import time


def greet_user(username):  # parameter ()
    """Display a simple greeting"""
    print(f"hello, {username.title()}!")


greet_user("Fedik")  # argument ()


# Try it yourself
# 8.1
def display_message():
    print("HI! I am just learning content in chapter 8!")


display_message()


# 8.2
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}!")


favorite_book("LOTR")


# pets.py


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("hamster", "harry")
describe_pet("dog", "willie")
describe_pet(animal_type="hamster", pet_name="harry")


def describe_peet(pet_name, animal_type="dog"):  # default parameter
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_peet("willie", "cat")
"""default parameter sa da zmenit v argumente, alebo nenapisat vobec a automaticky tam vypise default volbu parametru"""


# Try it yourself
# 8.3, 8.4
def make_shirt(text, size="large"):
    print(f"Shirt's size is {size} and it will be printed '{text}' on it!")


make_shirt("I love python")
make_shirt("I love python", "medium")
make_shirt("I love to code", size="small")


# 8.5
def describe_city(city, country="Slovakia"):
    print(f"{city} is in {country}!")


describe_city("Trencin")
describe_city("Bratislava")
describe_city("Praha", "Czech Republic")


# formatted_name
def get_formatted_name(first_name, last_name, middle_name=None):
    """Return a full name, neatly formatted."""

    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()


musician = get_formatted_name("john", "hooker")
print(musician)
musician = get_formatted_name("john", "hooker", "lee")
print(musician)


# person
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""

    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person("jimi", "hendrix", age=27)
print(musician)


# greeter
def get_formatted_namee(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# This is an infinite loop !
while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == "q":
        break

    l_name = input("Last name: ")
    if l_name == "q":
        break

    formatted_name = get_formatted_namee(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


# Try it yourself
# 8.6
def city_country(city, country):
    definition = f"{city}, {country}"
    return definition


print(city_country("santiago", "chile").title())
print(city_country("brno", "czech republic").upper())
print(city_country("bosaca", "slovakia").capitalize())


# 8.7, 8.8 Album
def make_album(artist, album, songs=None):
    albumized = {"artist": artist, "album": album}
    if songs:
        albumized["songs"] = songs

    return albumized


first = make_album("Nirvana", "Baby", 8)
second = make_album("lady gaga", "paparazzi", 5)
third = make_album("rytmus", "cigan", 8)

print(f"{first}\n{second}\n{third}")

while True:
    artist = input("Artist: ").lower()
    if artist == "q":
        break

    album = input("Album: ").lower()
    if album == "q":
        break

    songs = input("Songs: ")
    if songs == "q":
        break

    songs = int(songs)

    albumizedd = make_album(artist, album, songs)
    print(albumizedd)
    print("Type 'q' to quit the program.")


# greet_users


def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        if len(name) >= 6:
            print(f"The '{name.title()}' is...")
            texty = "too long!!!"
            for char in texty:
                print(char, end="")
                print()
                time.sleep(0.25)
        else:
            print(f"Hello, {name.title()}!")


usernames = ["hannah", "ty", "margot", "justinka", "jozo", "fero"]
greet_users(usernames)


# printing_models
# Start with some designs that need to be printed.
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

# Simulate printing each design, until none are left.
# Move each deisgn to completed_models after printing.
while unprinted_designs:
    current_designs = unprinted_designs.pop()
    print(f"Printing model: {current_designs}")
    completed_models.append(current_designs)

# Display all completed models.
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)


# Try it yourself
# 8.9, 8.10, 8.11
def send_messages(messages, sent_messages):
    while messages:
        moved_item = messages.pop()
        sent_messages.append(moved_item)
        print(moved_item.capitalize())


sent_messages = []
messages = ["hit me up", "yo!", "that's low-key bad", "no way"]

send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)


# # pizza ARBITRARY NUMBER OF ARGUMENTS
# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")


# make_pizza("pepperoni")
# make_pizza("mushrooms", "green peppers", "extra cheesse")


# Mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# try it yourself
# 8.12
def make_sandwich(*ingredients):
    print("Making the sandwich for you with these ingredients:")
    for ingredient in ingredients:
        print(ingredient.title(), end="")
        print()


make_sandwich("salt")
make_sandwich("spinach", "cheese", "geci", "ketchup")
make_sandwich("tuna", "raviolli")


# 8.13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a use."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "Frederik", "Kukuca", gender="man", race="white", hobby="python"
)
for user, profile in user_profile.items():
    print(f"{user.title()} - {profile.title()}")


# 8.14
def describe_car(manufacturer, model, **details):
    details["manufakturer"] = manufacturer
    details["model"] = model
    return details


car = describe_car("subaru", "outback", color="blue", tow_package=True, gear="manual")
for what, it in car.items():
    print(f"{what.title()} - {it}")


"""exercises........
##
###
####
"""
