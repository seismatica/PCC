class Restaurant():
    """A class representing a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print the restaurant's name and cuisine type"""
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        """Display a message that the restaurant is open"""
        print(self.cuisine_type + " restaurant " + self.restaurant_name + " is open!")


def print_restaurant(restaurant):
    """Receives a restaurant instant
    , print restaurant attributes
    , and invoke methods that print restaurant description and display restaurant is open"""
    print(restaurant.restaurant_name, restaurant.cuisine_type)
    restaurant.describe_restaurant()
    restaurant.open_restaurant()


while True:
    name = input("Input name of restaurant (type 'q' to quit): ")
    if name.lower() == "q":
        break
    cuisine = input("Input cuisine type of restaurant (type 'q' to quit): ")
    if cuisine.lower() == "q":
        break
    restaurant = Restaurant(name, cuisine)
    print_restaurant(restaurant)
