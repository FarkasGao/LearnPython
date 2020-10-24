noodles = ["Tomato noodles", "Bone noodles", "Lamian noodles"]
finish_sandwiches = []

while len(noodles) != 0:
    noodle = noodles.pop()
    print(f"I made your {noodle}")
    finish_sandwiches.append(noodle)
    
print(noodles)
print(finish_sandwiches)