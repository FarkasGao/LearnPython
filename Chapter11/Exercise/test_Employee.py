import unittest

from employee import Employee

filename = '11_3.py'

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('y', 'g', 15000)
        print(self.employee.annual_salary)
        
    def test_give_default_raise(self):
        self.employee.give_raise()
        print(self.employee.annual_salary)
    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        print(self.employee.annual_salary)
        
if __name__ == "__main__":
    unittest.main()