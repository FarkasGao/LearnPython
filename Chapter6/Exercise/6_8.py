pet1 = {
    'name': 'benben',
    'master': 'xiaowang'
    }
pet2 = {
    'name': 'lisa',
    'master': 'xiaohua',
    }
pet3 = {
    'name': 'dazhuang',
    'master': 'xiaoming'
    }
    
pets = []
pets.append(pet1)
pets.append(pet2)
pets.append(pet3)

for pet in pets:
    print(pet['master'])
    print(pet['name'])