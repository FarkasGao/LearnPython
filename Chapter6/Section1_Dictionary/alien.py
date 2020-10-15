alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

your_point = 0
your_point += alien_0['points']
print(f"You just earned {your_point} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}

alien_1['color'] = 'red'
alien_1['points'] = 10

print(alien_1)

print(f"The alien is {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

alien_0['speed'] = 'medium'
print(f"Original position: {alien_0['x_position']}")

#向右移动外星人
#根据当前速度确定外星人向右移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #这个外星人的移动速度一定很快
    x_increment = 3
#新位置为旧位置加上移动距离
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

del alien_0['points']
print(alien_0)