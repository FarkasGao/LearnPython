filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    pass
else:
    print(contents.lower().count('the'))
    print(contents.lower().count('the '))