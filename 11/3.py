import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        first = "Khanh"
        last = "Nguyen"
        salary = 10000
        self.employee = Employee(first, last, salary)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 15000)

    def test_give_custom_raise(self):
        self.employee.give_raise(2000)
        self.assertEqual(self.employee.salary, 12000)


if __name__ == "__main__":
    unittest.main()