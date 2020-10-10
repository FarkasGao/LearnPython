name = ['Albert Einstein', 'Bill Gates', 'Da Vinci']
print(f"I'm going to invite {name[0]}, {name[1]} and {name[2]} to dinner")
leave = name.pop()
print(f"Just learned that {leave} couldn't come for some reason")
name.append('My girl')
print(f"I'm going to invite {name[0]}, {name[1]} and {name[2]} to dinner")
print("I just found a bigger table")

name.insert(0, 'Lu Fei')
name.insert(2, 'Di Ren Jie')
name.append('Jin Yong')
print(f"Now I'm going to invite {name[0]}, {name[2]} and {name[5]} to dinner, too")
