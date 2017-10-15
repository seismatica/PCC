import json
from string_match import match
from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world.maps import World
import pygal.style as ps


def pick_partial_match(country, partial_matches):
    """
    Input: list of partial matches to a given country (as list of [code, name in COUNTRIES, longest match string])
    Output: Ask user to pick the closest match to that country from the top 3 matches. Return the code of the matched
    country. If no match was found, return None.
    """
    # Sort partial matches items based on longest match
    partial_matches.sort(key=lambda l: len(l[2]), reverse=True)

    # Display 3 longest matches
    print("-----")
    print("Top 3 matches of " + country + ":")
    top_three_matches = partial_matches[0:3]
    for index, item in enumerate(top_three_matches):
        print(index+1, "-", item[1], "(" + item[2] + ")")

    # Ask user to pick the best match from the top 3 matches based on input index, return None if no match was found
    while True:
        chosen_index = input("Pick a number of the closest match (type 'n' if no match was found): ")
        if chosen_index not in ['1', '2', '3', 'n']:
            print('Invalid input')
        elif chosen_index == 'n':
            return None
        else:
            code = top_three_matches[int(chosen_index) - 1][0]
            return code


def excluded_countries(name):
    """
    Check if a country has keywords that renders it irrelevant
    :param name: Input country name (str)
    :return: True if the country name has any of the excluded keywords
    """
    excluded_keywords = ['world', 'states', 'income', 'countries', 'area', 'union', 'members', '(', ')']
    for keyword in excluded_keywords:
        if keyword in name.lower() and name.lower() != 'united states':
            return True


def strip_country(country):
    """
    Strip country with extraneous words so a better match can be found
    :param country: Input country
    :return: Country with some keywords stripped
    """
    stripped_keywords = ['Republic']
    for keyword in stripped_keywords:
        country = country.replace(keyword, '')
    return country


def convert_to_country_code(country):
    """
    Input: a given country (str)
    Output: compare given country to countries in pygal's COUNTRIES dict. Return a 2-digit code from the dict
    if a complete match was found. Else, display partial matches for user to pick the best match out of three,
    and return the code for that partial match. If no complete or partial match was found, return None.
    """

    partial_matches = []
    for code, name in COUNTRIES.items():
        # Return country code if complete match found
        if name.lower() == country.lower():
            return code
        # Store partial match just in case
        else:
            # Return the longest match between the 2 country names
            country_stripped = strip_country(country)
            partial_match = match(name, country_stripped).strip()
            # Collect code, COUNTRIES name, and given country name as a list item
            partial_matches.append([code, name, partial_match])

    # Return country code after asking user to pick from the top 3 matches of the given country (return None if no
    # match was found)
    code = pick_partial_match(country, partial_matches)
    return code


def build_pop_dict(filename, year):
    """
    Input: json file name whose format (list of dictionaries, each with key of country name, country population,
    year, etc. and their corresponding values), and given year
    Output: a dictionary with 2-digit country codes as key, as corresponding population at the given year as value.
    A None key is present to represent countries that cannot be found in pygal's COUNTRIES dict"""
    with open(filename) as file_content:
        world_pop = json.load(file_content)
        world_pop_year = {}

        # Import existing country to code dictionary stored in json file (from previous run)
        # If file does not exist, create a new dict to store country to code conversions
        try:
            with open("country_to_code.json", "r") as country_code_content:
                country_code_dict = json.load(country_code_content)
        except FileNotFoundError:
            country_code_dict = {}

        for item in world_pop:
            # Get population and country values from country item in read file
            if item['Year'] == str(year):
                population = item['Value']
                country = item['Country Name']

                # If country name contains words that indicate it's not a country (e.g. EOCD nations),
                # move on to the next country
                if excluded_countries(country):
                    continue

                # If country is not in the country to code dict,
                # convert the country name to code and store the pair in the dict
                if country not in country_code_dict:
                    country_code = convert_to_country_code(country)
                    country_code_dict[country] = country_code
                # If country is already in the country to code dict,
                # get the corresponding code from the dict
                else:
                    country_code = country_code_dict[country]

                # Store the country code and corresponding population in the given year as a pair in a dict
                world_pop_year[country_code] = round(float(population))
        with open("country_to_code.json", "w") as country_code_content:
            json.dump(country_code_dict, country_code_content)

    return world_pop_year


def main():
    # Get dict of code to population at year 2010 for plotting
    world_pop_2010 = build_pop_dict("population_data.json", 2010)

    # Divide dict into three smaller dicts corresponding to population levels (low, medium, high)
    low_pop_2010, medium_pop_2010, high_pop_2010 = {}, {}, {}
    for code, pop in world_pop_2010.items():
        if pop < 10000000:
            low_pop_2010[code] = pop
        elif pop < 1000000000:
            medium_pop_2010[code] = pop
        else:
            high_pop_2010[code] = pop

    # Create pygal maps plotting object
    map_style = ps.DarkSolarizedStyle
    wm = World(style=map_style)
    wm.title = 'World populations'

    # Add the shading for countries in each population level
    wm.add('0-10m', low_pop_2010)
    wm.add('10m-1b', medium_pop_2010)
    wm.add('>1b', high_pop_2010)

    # Render graph to svg file
    wm.render_to_file('world.svg')


main()
