#alien_0 = {'color': 'green', 'points': 5}
#print(alien_0)
#new_points = alien_0['points']
#print(f"You just earned {new_points} points!")
#alien_0['x_position'] = 0
#alien_0['y_position'] = 25
#print(alien_0)

#alien_0 = {}
#alien_0['color'] = 'green'
#alien_0['points'] = 5
#print(alien_0)

#alien_0 = {'color': 'green'}
#print(f"The alien is {alien_0['color']}.")
#alien_0['color'] = 'yellow'
#print(f"The alien is now {alien_0['color']}.")


#alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
#print(f"Original position: {alien_0['x_position']}")

#if alien_0['speed'] == 'slow':
    #x_increment = 1
#elif alien_0['speed'] == 'medium':
    #x_increment = 2
#else:
    #x_increment = 3

#alien_0['x_position'] += x_increment

#print(f"New position: {alien_0['x_position']}")


#alien_0 = {'color': 'green', 'points': 5}
#print(alien_0)
#del alien_0['points']
#print(alien_0)


#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'rust',
#    'phil': 'python'
#}
#language = favorite_languages['sarah'].title()
#print(f"Sarah's favorite language is {language}.")


#alien_0 = {
#    'color': 'green', 
#    'speed': 'slow'
#}
#point_value = alien_0.get('points')
#print(point_value)



#person_0 = {
#    'first_name': 'frederik',
#    'last_name': 'kukuca',
#    'age': '24',
#    'city': 'bratislava'
#}
#favorite_number = {
#    'leopold': 13,
#    'sralo': 25,
#    'pindo': 5,
#    'jebo': 1,
#    'kremes': 88
#}
#print(favorite_number)
"""
python_code = {
    'def': 'funkcia',
    'for i in list': 'vyber elementu zo zoznamu a priradenie roboty',
    'tuple': 'zoznam ktory sa neda modifikovat',
    'glossary': 'aktualny slovnik(forma dictionary zoznamu)',
    'variable': 'premenna ktorej urcim hodnotu'
}

print(
    f"def: {python_code['def'].title()}\n"
    f"for i in list: {python_code['for i in list'].title()}\n"
    f"tuple: {python_code['tuple'].title()}\n"
    f"glossary: {python_code['glossary'].title()}\n"
    f"variable: {python_code['variable'].title()}"
)


python_code['set'] = 'list ktory nema duplikaty values a nema poradie'
python_code['enamurate'] = 'nahradza elegantnejsie ,,for i in range(len(list))'
python_code['range'] = 'vyhlada indexy s ich values v liste'
python_code['not in / in'] = 'skontroluje pritomnost variable v liste'
python_code['sorted / sort'] = 'abecedne zoradi list pre ucinok kodu / abecedne zoradi list natrvalo'
for key, values in python_code.items():
    print(f"{key.title()} : {values.title()}")


rivers = {
    'dunaj': 'slovensko',
    'temza': 'anglicko',
    'nil': 'egypt'
}
for key, value in rivers.items():
    print(f"The {key.title()} runs though the country named {value.title()}")


alien_0 = {
    'color': 'green',
    'points': 5
}
alien_1 = {
    'color': 'yellow',
    'points': 10
}
alien_2 = {
    'color': 'red',
    'points': 15
}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

"""

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")