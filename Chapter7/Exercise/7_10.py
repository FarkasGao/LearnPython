print("If you could visit one place in the world, where would you go?")

list1=[]
while True:
    place = input(">")
    if place == 'quit':
        break
    list1.append(place)
    
for place in list1:
    print(place)