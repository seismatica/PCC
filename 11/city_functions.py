def print_city_country(city, country, population=""):
    """Print 'city, country' from input city and country"""
    if population:
        formatted_city_country = city + ", " + country + " - population " + str(population)
    else:
        formatted_city_country = city + ", " + country
    return formatted_city_country


