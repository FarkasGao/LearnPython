import json

filename = 'user_name.py'
    
def write_user():
    with open(filename, 'w') as f:
        username = input("What's your name? ")
        json.dump(username, f)
        print(f"We'll remember you when you come back")
        
def greet_user():
    """问候用户, 并指出起名字"""   
    try:
        with open(filename) as f:
            content = json.load(f)
    except FileNotFoundError:
        write_user()
    else:
        print(f"Welcome {content}!")
       
greet_user()