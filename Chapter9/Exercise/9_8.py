class User:
    def __init__(self, first_name, last_name, sex, country):
        self.name = f"{first_name} {last_name}"
        self.sex = sex
        self.country = country
        
    def describe_user(self):
       print(f"""information as follow:
    name = {self.name}
    sex = {self.sex}
    country = {self.country.title()}""")
               
    def greet_user(self):
        print(f"Hello! {self.name}")

class Privileges:
    """Administrator privileges"""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        
    def show_privileges(self):
        print(self.privileges)
        
class Admin(User):
    def __init__(self, first_name, last_name, sex, country, privileges):
        super().__init__(first_name, last_name, sex, country)
        self.privileges = privileges

privileges = Privileges()
admin = Admin('xiao', 'wang', 'man', 'china', privileges)
admin.privileges.show_privileges()