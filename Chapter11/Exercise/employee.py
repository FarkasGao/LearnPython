class Employee:
    def __init__(self, last_name, first_name, annual_salary):
        self.annual_salary = annual_salary
        
    def give_raise(self, salary_raise=5000):
        self.annual_salary += salary_raise