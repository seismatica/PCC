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
        print("\n")

    def greet_user(self):
        """Greet user"""
        print("Hello " + self.first_name + " " + self.last_name + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age, hometown):
        super().__init__(first_name, last_name, age, hometown)
        # From this point on, Admin can use attribute names of user
        self.privileges = []

    def show_privileges(self):
        print(self.first_name + " " + self.last_name + "'s priveleges are: ")
        for privilege in self.privileges:
            print(privilege.title())
        print("\n")


admin = Admin("Khanh", "Nguyen", 27, "Ho Chi Minh City")
admin.describe_user()
admin.privileges = ["can add post", "can delete post", "can ban user"]
admin.show_privileges()
