import json

#如果以前储存了用户名，就加载他
#否则，提示用户输入用户名并储存他
filename = 'user_name.py'

try:
    with open(filename) as f:
        content = json.load(f)
except FileNotFoundError:
    with open(filename, 'w') as f:
        username = input("What's your name? ")
        json.dump(username, f)
        print(f"We'll remember you when you come back")
else:
    print(f"Welcome {content}!")