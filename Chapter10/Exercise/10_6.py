print("Give me two numbers, and I will add them up.")
print("(Enter 'q' to exit)")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("second number: ")
    if second_number == 'q':
        break
        
    try:
        number = int(first_number) + int(second_number)
    except ValueError:
        print("You should enter a number")
    else:
        print(number)