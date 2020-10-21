cities = {
    'bei jing' :{
        'country': 'china',
        'population': 21536000,
        'fact': 'house price is very expensive'
        },
    'tian jin' :{
        'country': 'china',
        'population': 15618300,
        'fact': 'there is very slow rhythm'
        }
    }
        
for name,city in cities.items():
    print(f"{name} is a interest city, It is located in {city['country']},"
    f"It has {city['population']} people,There is a fact:{city['fact']}.")