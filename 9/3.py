class User:
    """"""
    def __init__(self, first_name, last_name, age, hometown):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hometown = hometown

    def describe_user(self):
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
        print("Age: " + str(self.age))
        print("Hometown: " + self.hometown)

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name + "!")


while True:
    first_name = input("Input your first name (type q to quit): ")
    if first_name.lower() == "q":
        break
    last_name = input("Input your last name (type q to quit): ")
    if last_name.lower() == "q":
        break
    age = input("Input your age (type q to quit): ")
    if age.lower() == "q":
        break
    hometown = input("Input your hometown (type q to quit): ")
    if hometown.lower() == "q":
        break

    user = User(first_name, last_name, age, hometown)
    user.describe_user()
    user.greet_user()