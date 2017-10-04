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


class IceCreamStand(Restaurant):
    """Represent an ice cream stand, which inherits from Restaurant class.
    Add additional attribute to store ice cream flavors and method to print those flavors"""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Initialize ice cream stand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """Display ice cream flavors"""
        for flavor in self.flavors:
            print(flavor.upper())


ice_cream_stand = IceCreamStand("Pho King", "Vietnamese", ["vanilla", "chocolate"])
ice_cream_stand.display_flavors()