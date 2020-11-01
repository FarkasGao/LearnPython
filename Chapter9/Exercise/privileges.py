from Admin import User 

class Privileges:
    """Administrator privileges"""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        
    def show_privileges(self):
        print(self.privileges)
        
class Admin(User):
    def __init__(self, first_name, last_name, sex, country):
        super().__init__(first_name, last_name, sex, country)
        self.privileges = Privileges()