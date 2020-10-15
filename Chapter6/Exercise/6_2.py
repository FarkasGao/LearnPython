favorite_numbers = {
    'me': 8,
    'DaA': 1,
    'DaB': 2,
    'DaC': 3,
    'DaD': 4
    }

for favorite_number in favorite_numbers:
    if favorite_number == 'me':
        print("My favorite number is 8")
    else:
        print(f"{favorite_number}'s favorite number is {favorite_numbers.get(favorite_number)}")