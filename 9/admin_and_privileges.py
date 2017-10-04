from only_user import User


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