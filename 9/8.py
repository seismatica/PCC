class User():
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
        print("Hometown: " + self.hometown + "\n")

    def greet_user(self):
        """Greet user"""
        print("Hello " + self.first_name + " " + self.last_name + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    """Describe an admin user which is the same as a general user but with
    extra privileges"""
    def __init__(self, first_name, last_name, age, hometown):
        """Initialize admin's information"""
        super().__init__(first_name, last_name, age, hometown)
        # From this point on, Admin can use attribute names of user
        self.privileges = Privilege(self.first_name, self.last_name)
        # Pass Admin's attributes as init argument for privilege


class Privilege():
    """Describe privileges of a user"""
    def __init__(self, first_name, last_name, items=[]):
        self.first_name = first_name
        self.last_name = last_name

    def show_privileges(self):
        """Display user's privileges"""
        if self.items:
            print(self.first_name + " " + self.last_name + "'s privileges are: ")
            for privilege in self.items:
                print(privilege.title())
        else:
            print(self.first_name + " " + self.last_name + " has no privilege\n")


admin = Admin("Khanh", "Nguyen", 27, "Ho Chi Minh City")
admin.describe_user()
admin.privileges.items = ["can ban user"]
admin.privileges.show_privileges()
