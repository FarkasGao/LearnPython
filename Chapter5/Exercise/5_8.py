Users = ['admin', 'gao', 'farkas', 'gage', 'fw']

if Users:
    for User in Users:
        if User == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {User},thank you for logging in again.")
else:
    print("We need to find some users!")