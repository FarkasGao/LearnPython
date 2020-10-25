def city_country(city_name, city_country = 'china'):
    city_with_country = f"{city_name.title()}, {city_country.title()}"
    return city_with_country

cities = []    
cities.append(city_country('tian jin'))
cities.append(city_country('shang hai'))
cities.append(city_country('paris', 'france'))

for city in cities:
    print(city) 