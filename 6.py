def city_country(city, country):
    """This function takes in a city and a country, and outputs them next to each other, separate by a comma"""
    city_and_country = city + ", " + country
    return city_and_country.title()


def notify_invalid_input(user_input):
    """This function notifies user if their input was invalid (" " or "")"""
    if user_input == " " or user_input == "":
        print("Invalid input.\n")


def city_input():
    """This function asks user to input a city and a country, and display them using city_country function"""
    city_active = True
    while city_active:
        city = input("Input your city: ")
        if city == " " or city == "":
            notify_invalid_input(city)  # returns to city input prompt
        elif city.lower() == "quit":
            city_active = False  # exits city input loop
        #  city input is not quit or invalid, move on to country prompt
        else:
            country_active = True
            while country_active:
                country = input("Input your country: ")
                if country == " " or country == "":
                    notify_invalid_input(country)  # and returns to country input prompt
                elif country.lower() == "quit":
                    country_active = False
                    city_active = False  # exits both country and city input loops
                else:
                    city_display = city_country(city, country)
                    print(city_display)
                    country_active = False  # exits country input loop and returns to city input prompt


city_input()
