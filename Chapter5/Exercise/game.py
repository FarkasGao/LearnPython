#I just need Let it go first

#A good decision, And now I can finish it, A simple game
import random

your_money = 10
list1 = ['green', 'yellow', 'red']
while (True):
    if your_money == 0:
        print("you die")
        print("Do you want to restart the game?")
        if input().lower() == 'yes':
            your_money = 10
        else: 
            break
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
        random.shuffle(list1)
        print(list1)
        print("Please input 1 , 2 or 3.")
        your_money -= 5
        while time < 5:
            try:#程序出错时不结束而是完成特定事
                target = int(input(""))-1
            except Exception as e:
                print("please enter a number")
                target = -1
            if target>2 or target<0:
                print("Please input 1 , 2 or 3.") 
            else:
                time += 1
                Hit = list1[target]
                if Hit == 'green':
                    score += 1
                if Hit == 'yellow':
                    score += 3
                if Hit == 'red':
                    score += 5
        if score == 25:
            your_money += 15
            print("You win $15")
        if score < 25 and score > 19:
            your_money += 10
            print("You win $10")
        if score < 20 and score > 14:
            your_money += 5
            print("You win $5")
    elif answer == "no":
        break
print("Game end")