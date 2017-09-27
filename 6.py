def city_country(city, country):
    """This function takes in a city and a country, and outputs them next to each other, separate by a comma"""
    print(city + ", " + country)


def notify_invalid_input(user_input):
    """This function notifies user if their input was invalid (" " or "")"""
    if user_input == " " or user_input == "":
        print("Invalid input.\n")


def city_input():
    """This function asks user to input a city and a country, and display them using city_country function"""
    active = True
    while active:
        city = input("Input your city: ")
        if city == " " or city == "":
            notify_invalid_input(city)  # returns to city input prompt
        elif city.lower() == "quit":
            active = False  # exits city input loop
        else:
            while active:
                country = input("Input your country: ")
                if country == " " or country == "":
                    notify_invalid_input(country)  # and returns to country input prompt
                elif country.lower() == "quit":
                    active = False  # exits both country and city input loops
                else:
                    city_country(city, country)
                    active = False  # exits both country and city input loops


city_input()
