class Employee():
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, raise_amt=5000):
        self.salary += raise_amt  # Does not return anything -> cannot be assigned to another variable!