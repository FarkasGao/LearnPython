foods = ['noodle', 'rice', 'cake']
friend_foods = foods[:]

foods.insert(3, 'juice')
friend_foods.append('milk')

print("My favorite food are")
for food in foods:
    print(food,end=' ')
    
print("\n")
print("My friend's favorite pizzas are")
for food in friend_foods:
    print(food,end=' ')