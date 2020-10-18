favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
names =  ['jen', 'sarah', 'edward', 'phil', 'A', 'B', 'C']

for name in names:
    if name in favorite_languages:
        print(f"Thanks for you vote, {name}.")
    else:
        print(f"{name},please take this vote.")