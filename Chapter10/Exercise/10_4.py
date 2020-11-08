filename = 'visitor_list.txt'

with open(filename, 'a') as file_object:
    while True:
        name = input('please input you name(input "quit" to quit this cycle):')
        if name == 'quit':
            break
        print(f'Welcome! {name}')
        name += "\n"
        file_object.write(name)
        