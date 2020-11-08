print("Give me two numbers, and a operational character, then I will add them up.")
print("(Enter 'q' to exit)")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    operational_character = input("operational number: ")
    if operational_character == 'q':
        break
    second_number = input("second number: ")        
    if second_number == 'q':
        break
    
    if operational_character == '+':
        try:
            number = int(first_number) + int(second_number)
        except ValueError:
            print("You should enter a number")
        else:
            print(number)
    elif operational_character == '-':
        try:
            number = int(first_number) - int(second_number)
        except ValueError:
            print("You should enter a number")
        else:
            print(number)
    elif operational_character == '*':
        try:
            number = int(first_number) * int(second_number)
        except ValueError:
            print("You should enter a number")
        else:
            print(number)
    elif operational_character == '/':
        try:
            number = int(first_number) / int(second_number)
        except ValueError:
            print("You should enter a number!")
        except ZeroDivisionError:
            print("You can't division by zero!")
        else:
            print(number)
    else:
        print('Please enter "+", "-", "*" or "/".')