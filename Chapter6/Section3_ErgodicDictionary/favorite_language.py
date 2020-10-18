favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
    
for name,language in favorite_languages.items():
    print(f"{name}'s favorite languages is {language.title()}")
    
print("print name:")
for name in favorite_languages.keys():
    print(name.title())
    
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
        
if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")
    
print("\n")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()},thank you for take the poll")