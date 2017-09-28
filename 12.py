def print_sandwich_ingredients(*ingredients):
    print("You're ordering a sandwich with: ")
    for ingredient in ingredients:
        print("\t- " + ingredient.title())


def main():
    print_sandwich_ingredients("lettuce", "tomato", "bacon")
    print_sandwich_ingredients("cheese", "lettuce")
    print_sandwich_ingredients("cold cuts")
    print_sandwich_ingredients()


main()