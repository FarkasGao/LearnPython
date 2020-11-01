from random import randint

class Die:
    def __init__(self):
        self.sides = 6
    
    def roll_die(self):
        i = 0
        while i != 6:
            print(randint(1,self.sides))
            i += 1
        
    def change_sides(self, sides):
        self.sides = sides

die = Die()
die.roll_die()

die.change_sides(10)
die.roll_die()

die.change_sides(20)
die.roll_die()