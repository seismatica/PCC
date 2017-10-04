class User:
    """Represent a user profile"""

    def __init__(self, first_name, last_name, age, hometown):
        """Initialize user's information"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hometown = hometown
        self.login_attempts = 0

    def describe_user(self):
        """Display user's information"""
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
        print("Age: " + str(self.age))
        print("Hometown: " + self.hometown)

    def greet_user(self):
        """Greet user"""
        print("Hello " + self.first_name + " " + self.last_name + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("Khanh", "Nguyen", 27, "Ho Chi Minh City")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
