topping = []
client = ''

while True:
    client = input('Please enter ingredients you would like to add: ')
    if client == 'quit':
        break
    topping.append(client)
    print(f"We will add {client} to your pizza.")