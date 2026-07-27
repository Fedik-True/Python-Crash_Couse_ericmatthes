players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[0:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
my_foods.append('canoli')
friend_foods.append('ice cream')
print(f"My favorite foods are:\n {my_foods}")
print(f"\nMy friend's favorite foods are:\n {friend_foods}")

print(f"The first three items in the list are: {my_foods[:3]}")
print(f"The three items from the middle of the list are: {my_foods[1:4]}")
print(f"The last three items from the list are: {my_foods[2:5]}")

pizzas = ['salami', 'prosciuto', 'hawaii']
friend_pizzas = ['salami', 'prosciuto', 'hawaii']
pizzas.append('gazdovska')
friend_pizzas.append('rukola')
for pizza in pizzas:
    print(f"My favorite pizzas are: {pizza[:]}")
for pizza in friend_pizzas:
    print(f"My friend's favorite pizzas are: {pizza[:]}")