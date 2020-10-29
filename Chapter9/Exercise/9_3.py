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
        
        
target1 = User("xiao", "li", "man", "china")

target1.describe_user()
target1.greet_user()