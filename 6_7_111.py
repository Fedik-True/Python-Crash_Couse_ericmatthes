"""
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    

jedna1 = {
    'cicka': 'dlha',
    'kokotik': 'kratky',
    'ramena': 'chlpate'
}
dva2 = {
    'cigan': 'jebly',
    'rom': 'klamar',
    'vajda': 'boss'
}
tri3 = {
    'geno': 'dobre',
    'semeno': 'zle',
    'geci': 'madarske'
}
alls = [jedna1, dva2, tri3]
for dictionary in alls:
    for veci, value in dictionary.items():
        print(f"\nToto je {veci.title()}:")
        print(f"\tA znamena to toto: {value.upper()}")

pets = {
    'macka': {
        'race': 'sphinx',
        'color': 'pale',
        'owner': 'fedik'
    },
    'dog': {
        'race': 'bulterier',
        'color': 'white',
        'owner': 'justik'
    },
    'snake': {
        'race': 'python',
        'color': 'black',
        'owner': 'wilds'
    }
}

for pet_name, pet_info in pets.items():
    print(f"\nThis is a {pet_name.title()}.")
    info = f"He is a {pet_info['race']} and he's {pet_info['color']}, he belongs to {pet_info['owner']}"
    print(info)


favorite_places = {
    'fedik': ['barcelona', 'madrid', 'libanon'],
    'justik': ['trencin', 'bratislava', 'nitra'],
    'chrustik': ['praha', 'brno', 'ostrava']
}
for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite placec:")
    for place in places:
        print(f"\t{place.title()}")

"""
cities = {
    'trencin': {
        'country': 'slovakia',
        'population': 55000,
        'language': 'slovak',
        'area_km2': 82,
        'founded': 1111,
        'capital': False,
        'river': 'vah',
        'timezone': 'cet'
    },
    'praha': {
        'country': 'czech republic',
        'population': 1300000,
        'language': 'czech',
        'area_km2': 496,
        'founded': 885,
        'capital': True,
        'river': 'vltava',
        'timezone': 'cet'
    },
    'warsaw': {
        'country': 'poland',
        'population': 1800000,
        'language': 'polish',
        'area_km2': 517,
        'founded': 1300,
        'capital': True,
        'river': 'vistula',
        'timezone': 'cet'
    }
}

order = ['country', 'population', 'area_km2', 'language', 'founded', 'capital', 'river', 'timezone']

for city, info in cities.items():
    print(f"=== {city.title()} ===")

    density = info['population'] / info['area_km2']

    for key in order:
        value = info[key]
        
        if key == 'population':
            value = f"{value:,}"
        elif key == 'area_km2':
            value = f"{value} km2"
        elif key == 'capital':
            value = 'Yes' if value else 'No'

        print(f"{key.capitalize():<12}: {value}")
    
    print(f"{'Density':<12}: {density:.1f} per km2")
    print()