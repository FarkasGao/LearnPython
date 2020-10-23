while True:
    age = input("Please input your age: ")
    if age == 'quit':
        break
    elif int(age) < 3:
        print('You can visit it for free')
    elif int(age) <= 12 and int(age) >= 3:
        print('Your ticket price is $10')
    elif int(age) > 12:
        print('Your ticket price is $10')