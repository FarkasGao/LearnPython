#I just need Let it go first
import random

your_money = 10
List = ['green', 'yellow', 'red']
while (true):
    if your_money == 0:
        print("you die")
        print("Do you want to restart the game?")
        if input().lower() == 'yes':
            return false
        else: 
            return true
    time = 0 
    score = 0
    print("Five dollars for five shots")
    print("""PRIZE:
    <<< 25       score: $15 >>>
    <<< 20 to 24 score: $10 >>>
    <<< 15 to 19 score: $5  >>>
    
    green = 1; yellow = 3; red = 5""")
    print(f"You have ${your_money} now")
    print("Would you want to play this game?")
    answer = input().lower()
    if answer == "yes":
        while time ==5:
            target = int(input(""))-1
            if target>2 or target<0:
                print("Please input 1 , 2 or 3.")
                return
            time += 1
            Hit = list(target)
            if Hit == 'green':
                score += 1
            if Hit == 'yellow':
                score += 3
            if Hit == 'red':
                score += 5
        if score == 25:
            your_money += 15
        if score < 25 and score > 19:
            your_money += 10
        if score < 20 and score > 14:
            your_money += 5