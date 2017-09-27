def city_country(city, country):
    """This function takes in a city and a country, and outputs them next to each other, separate by a comma"""
    print(city + ", " + country)


def user_input():
    """This function asks user to input a city and a country, and display them using city_country function"""
    active = True
    while active:
        city = input("Input your city: ")
        if city == " " or city == "":
            print("Invalid input.\n")
        else:
            country = input("Input your country: ")
            if country == " " or city == "":
                print("Invalid input.\n")
            else:
                city_country(city, country)

user_input()
