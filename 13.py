def build_profile(first, last, **user_info):
    """Build a profile of a person with provided first name, last name, and other info"""
    print(user_info)
    profile = {"first name": first, "last name": last}
    for key, value in user_info.items():
        profile[key] = value
    profile_print(profile)


def profile_print(profile):
    """Print user's info from their profile"""
    print("User's information: ")
    for key, value in profile.items():
        print("\t" + key.title() + ": " + str(value))


def main():
    build_profile(first="K", last="Nguyen", age=27, hometown="Ho Chi Minh City")


main()