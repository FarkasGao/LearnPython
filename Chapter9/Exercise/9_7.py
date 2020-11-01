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
        
class Admin(User):
    def __init__(self, first_name, last_name, sex, country):
        super().__init__(first_name, last_name, sex, country)
        self.privileges = ['can add post', 'can delete', 'can ban user']
        
    def show_privileges(self):
        print(self.privileges)
        
target1 = User("xiao", "li", "man", "china")

target1.describe_user()
target1.greet_user()

admin = Admin('xiao', 'wang', 'man', 'china')
admin.show_privileges() 