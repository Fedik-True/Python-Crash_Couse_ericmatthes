# 7.8 / 7.9
import time

sandwich_orders = [
    "carbonara",
    "pastrami",
    "salami",
    "pastrami",
    "cheese",
    "ham",
    "pastrami",
]
finished_sandwiches = []
removed_sandwiches = []

print("---Deli has run out of pastrami!---")
pastrami_orders = True

while pastrami_orders:
    if "pastrami" in sandwich_orders:
        sandwich_orders.remove("pastrami")
    else:
        pastrami_orders = False

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich} sandwich order.")
    time.sleep(1)

print("\nFinished sandwiches!:")
for sandwich in finished_sandwiches:
    print(sandwich)

print(sandwich_orders)


# 7.10
dream_vacation = {}

has_something_to_say = True
while has_something_to_say:
    name = input("Tell me your name! ")
    dream = input("What's your dream vacation? ")

    dream_vacation[name] = dream

    repeat = input(
        "Would anyone else tell us about their dream vacation? (yes/no) "
    ).lower()
    if repeat == "no":
        has_something_to_say = False

print(dream_vacation)
