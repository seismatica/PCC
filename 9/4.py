class Restaurant():
    """A class representing a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print the restaurant's name and cuisine type"""
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        """Display a message that the restaurant is open"""
        print(self.cuisine_type + " restaurant " + self.restaurant_name + " is open!")

    def set_number_served(self, number_served):
        """Set number of customers served by provided amount"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Increment number of customers served by provided amount"""
        self.number_served += additional_served


restaurant = Restaurant("Pho King", "Vietnamese")
restaurant.number_served =50
print(restaurant.number_served)
restaurant.set_number_served(99)
print(restaurant.number_served)
restaurant.increment_number_served(10)
print(restaurant.number_served)