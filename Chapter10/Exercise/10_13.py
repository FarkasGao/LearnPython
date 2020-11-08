import json

def get_stored_username():
    """如果存储了用户名，就获取他"""
    filename = 'user.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
        
def get_new_username():
    """提示用户输入名"""
    username = input("What is your name?: ")
    filename = 'user.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username
        
def greet_user():
    '''问候用户，并指出其名字'''
    username = get_stored_username()
    if username:
        user = input(f"Is {username} your username: ")
        if user == "F":
            username = get_new_username()
            print(f"We'll remember you come back, {username}!")   
        else:    
            print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you come back, {username}!")
            
greet_user()