def city_country_population(city, country, population = ''):
    formatted = f"{city}, {country}"
    formatted = formatted.title()
    if population:
        formatted += f" - population {population}"
    return formatted