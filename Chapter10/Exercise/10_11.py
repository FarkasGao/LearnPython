import json

filename = "favorite_number.json"

try:
    with open(filename) as f:
        content = json.load(f)
except FileNotFoundError:
    with open(filename, 'w') as f:
        number = input("What's is your favorite number: ")
        json.dump(number, f) 
else:
    print(f"I know your favorite number! It's {content}")