import json

filename = 'fl.json'

with open(filename) as f:
    a = json.load(f)
    
print(a)