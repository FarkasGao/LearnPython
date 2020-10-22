number = input("How many people want to eat: ")
number = int(number)

if number > 8:
    print("Sorry,there aren't any vacant tables.")
elif number > 0:
    print("Yes,there have enought tables.")