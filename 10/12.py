import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        print("We'll remember you when you come back, " + username + "!")
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        while True:
            is_my_name = input("Is " + username + " your name (y/n)? ")
            if is_my_name.lower() == "y":
                print("Welcome back, " + username + "!")
            elif is_my_name == "n":
                get_new_username()
    else:
        get_new_username()


greet_user()
