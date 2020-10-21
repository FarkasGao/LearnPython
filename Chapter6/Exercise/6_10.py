favorite_numbers = {
    'me': [8,2],
    'DaA': [1,12],
    'DaB': [2,3],
    'DaC': [3,7],
    'DaD': [4,9]
    }

for name,favorite_number in favorite_numbers.items():
    print(f"{name}'s favorite number is")
    for number in favorite_number:
        print(number,end=' ')
    print("")