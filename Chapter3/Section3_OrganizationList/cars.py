cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()#按字母从小到大永久排序
print(cars)

cars.sort(reverse=True)#相反
print(cars) 

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))#临时排序

print("\nHere is the sorted list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)

letters = ['A', 'C', 'B', 'a', 'c', 'b', 'A']
print(sorted(letters))

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()#永久反转元素排列顺序
print(cars)

print(len(cars))#列表的长度