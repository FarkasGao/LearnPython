favorite_places = {
    'me' : ['tianjin', 'xizhang', 'jiangsu'],
    'daming' : ['beijing','shanghai'],
    'lingling' : ['beijing','neimeng']
    }
    
for name,place in favorite_places.items():
    print(f"{name}'s favorite places is",end=' ')
    for pla in place:
        print(pla.title(),end=' ')
    print() 