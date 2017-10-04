class User:
    """Represent a user's profile"""
    def __init__(self, first_name, last_name, **user_info):
        """Initialize user's information with variable additional info beyond first & last name"""
        self.first_name = first_name
        self.last_name = last_name
        for key, value in user_info.items():
            setattr(self, key, value)


user = User("K", "Nguyen", age=27, hometown="HCM")
print(user.age)