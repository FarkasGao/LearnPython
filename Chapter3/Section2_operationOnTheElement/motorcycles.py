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

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)