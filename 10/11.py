# Ask user for their favorite number, and print it from this file

import json


def input_number(file_name):
    """Ask user to input their favorite number and store it in a file"""
    while True:
        try:
            favorite_number = int(input("Input your favorite number (integer only): "))
        except ValueError:
            print("You did not input an integer.")
        else:
            with open(file_name, "w") as file_object:
                json.dump(favorite_number, file_object)
            break


def display_number(file_name):
    """Load favorite number from file and print it"""
    with open(file_name) as file_object:
        favorite_number = json.load(file_object)
        print("Your favorite number is: " + str(favorite_number))


def main():
    """Display user's favorite number from existing file.
    If file is not found, ask user to input their favorite number,
    then store it into a file and read it back to user"""
    file_name = "favorite_number.json"
    try:
        open(file_name)
    except FileNotFoundError:
        print(file_name + " not found")
        input_number(file_name)
        display_number(file_name)
    else:
        display_number(file_name)


main()
