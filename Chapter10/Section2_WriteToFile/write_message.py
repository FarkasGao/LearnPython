filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("""I love programming.
I love creating new games.\n""")
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")