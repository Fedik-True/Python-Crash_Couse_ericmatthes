"""
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

people = {
    'Jozo': 'rust',
    'Gadzo': 'c++',
    'Geco': 'c#'
}
favorite_languages.update(people)
for key, value in people.items():
    if key in favorite_languages:
        print(f"Hello {key.title()}!")
    elif key not in favorite_languages:
        print(f"You should join our poll {key.title()}!")
favorite_languages.update(people)
print(favorite_languages)