motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')#添加元素到末尾 
print(motorcycles)

letters = []

letters.append('A')
letters.append('B')
letters.append('C')

print(letters)

motorcycles.insert(0,'motor')
print(motorcycles)
#1
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)
#2
popped_motorcycle = motorcycles.pop()#弹出元素
print(motorcycles)
print(popped_motorcycle)
#3
popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(f"The second motorcycles I owned was a {popped_motorcycle.title()}.")
#4
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('yamaha')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")

letters = ['A', 'B', 'A']
letters.remove('A')
print(letters)