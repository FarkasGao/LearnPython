favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
    
print("The following language have been mentioned:")
for language in favorite_language.values():
    print(language.title())
    
print("\n")    
for language in set(favorite_language.values()):#set()是一个只包含不同元素的列表
    print(language.title()) 