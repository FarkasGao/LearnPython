import json

filename = "favorite_number.json"

def get_stored_number():
    try:
        with open(filename) as f:
            content = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return content

def get_your_favorite_number():
    with open(filename, 'w') as f:
        number = input("What's is your favorite number: ")
        json.dump(number, f) 
        
def favorite_number():
    number = get_stored_number()
    if get_stored_number():
        print(f"I know your favorite number! It's {number}")
    else:
        get_your_favorite_number()
        
favorite_number()