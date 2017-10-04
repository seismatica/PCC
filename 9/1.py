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


restaurant = Restaurant("Pho King", "Vietnamese")
print(restaurant.restaurant_name, restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()