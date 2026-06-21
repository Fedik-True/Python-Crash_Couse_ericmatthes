"""
pizzas = ['salami', 'prosciuto', 'hawaii']
for pizza in pizzas:
    print(f"I really like {pizza} pizza")

print("\nI really really love pizza!\n")

animals = ['dog', 'cat', 'panda']
for animal in animals:
    print(f"I adore {animal.title()}, because it is cute!")


pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
"""

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is:")
        print(f"\t{languages[0].title()}")