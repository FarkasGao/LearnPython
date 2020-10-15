Ordinals = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for Ordinal in Ordinals:
    print(Ordinal, end = ' ')
print("")
for number in numbers:
    print(number, end = ' ')
    
for number in numbers:
    if number == 1:
        print(number, "st")
    elif number == 2:
        print(number, "nd")
    elif number == 3:
        print(number, "rd")
    else:
        print(number, 'th')