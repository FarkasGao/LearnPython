filename = 'reason_for_like.txt'

with open(filename, 'a') as file_object:
    while True:
        reason = input('Why do you like programming(Enter "quit" to quit): ')
        if reason == 'quit':
            break
        reason += '\n'
        file_object.write(reason)