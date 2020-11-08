list1 = [1.65, 3.32, 4.92, 6.615, 8.265, 9.91, 11.56, 13.21]

a = 0.0355

list2 = [a, a*2, a*3, a*4, a*5, a*6, a*7, a*8]
num1 = 0
num2 = 0
for number in list2:
    num = number*number
    print(num, end = ' ')
    num1 += num
    
print(num1/8)   

print(list2)


print("----------------------")
for i in range(0,8):
    num = list1[i]*list2[i]
    print(num)
    num2 += num
print(num2/8)