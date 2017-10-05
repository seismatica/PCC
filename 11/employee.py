class Employee():
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, raise_amt=5000):
        self.salary += raise_amt

# employee = Employee("Khanh", "Nguyen", 10000)
# employee.give_raise(2000)
# print(employee.salary)