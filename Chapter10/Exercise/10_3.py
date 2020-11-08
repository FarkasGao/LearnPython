filename = 'guest.txt'

with open(filename, 'a') as file_object:
    name = input("Please input your name: ")
    name += '\n'
    file_object.write(name)