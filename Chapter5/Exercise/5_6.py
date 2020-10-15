age = int(input("Tell me his age:"))
if age < 2:
    print("He is a baby")
if age < 4 and age >= 2:
    print("He is a nesting")
if age < 13 and age >= 4:
    print("He is a child")
if age < 18 and age >= 13:
    print("He is a teenagers")
if age < 65 and age >=18:
    print("He is a adult")
if age >= 65:
    print("He is a aged")