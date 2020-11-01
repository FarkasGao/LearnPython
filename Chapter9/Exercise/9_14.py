from random import choice

lottery = [1,2,3,4,5,6,7,8,9,'a','b','c','d','e']

lottery_number = []
i=0
while i < 4:
    lottery_number.append(choice(lottery))
    i += 1
print(lottery_number)