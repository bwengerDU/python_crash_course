def formatted_city_name(city, country, population=0):
    """Module to format a given city and country name"""
    full_name = f"{city.title()}, {country.title()}"
    if population:
        full_name = f"{city.title()}, {country.title()} ~ Population {population.title()}"
    return full_name
