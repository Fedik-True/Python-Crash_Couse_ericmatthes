#requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#for requested_topping in requested_toppings:
#    if requested_topping == 'green peppers':
#        print("Sorry, we are out of green peppers right now.")
#    else:
#        print(f"Adding {requested_topping}!")
#print("\nFinished making your pizza!")

#requested_toppings = []
#if requested_toppings:
#    for requested_topping in requested_toppings:
#        print(f"Adding {requested_topping}.")
#    print("\nFinished making your pizza!")
#else:
#    print("Are you sure you want a plain pizza?")

#available_toppings = ['mushrooms', 'olives', 'green peppers',
#                      'pepperoni', 'pineapple', 'extra cheese']
#requested_toppings = ['mushrooms', 'frensh fries', 'extra cheese']
#for requested_topping in requested_toppings:
#    if requested_topping in available_toppings:
#        print(f"Adding {requested_topping}.")
#    else:
#        print(f"Sorry, we don't have {requested_topping}")
#print("\nFinished making your pizza!")



#usernames = ['fedosvk', 'fergass', 'feuel', 'elysium', 'admin']
#if not usernames:
#    print("We need to find some users.")
#for user in usernames:
#    if user == 'admin':
#        print("Hello admin, would you like to see a status report?")
#    else:
#        print(f"Hello {user.title()}, thank you for logging in again.")

#current_users = ['fero', 'jozo', 'gabo', 'pato', 'fifo']
#new_users = ['fero', 'finko', 'granko', 'pisko', 'fifo']
#for user in new_users:
#    if user.lower() in current_users:
#        print(f"The username {user} is already taken.")
#    else:
#       print(f"Greetings {user}!")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")