from restaurant import Restaurant


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
            print(flavor.title())


restaurant = Restaurant("Coq au vin", "French")
restaurant.describe_restaurant()
restaurant.open_restaurant()
ice_cream_stand = IceCreamStand("Pho King", "Vietnamese", ["vanilla", "chocolate"])
ice_cream_stand.display_flavors()