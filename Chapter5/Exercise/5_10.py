current_users = ['admin', 'Gao', 'farkas', 'gage', 'fw']
new_users = ['a', 'b', 'c', 'gao', 'admin']

for user in new_users:
    if user.lower() in current_users:
        print(f"{user} is alright been used")
    else:
        print(f"{user} is available")