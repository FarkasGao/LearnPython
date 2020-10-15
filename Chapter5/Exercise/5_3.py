import random

alien = ['green', 'yellow', 'red']
points = 0
alien_color = alien[random.randint(0,2)]

if alien_color == 'green':
    print('Good job! You get five points')
    points += 5
if alien_color == 'yellow':
    print('Good job! You get ten points')
    points += 10
if alien_color == 'red':
    print('Good job! You get fifteen points')
    points += 15