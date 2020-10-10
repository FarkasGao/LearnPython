language = ['c', 'c++', 'c#', 'java', 'javascript']

print(language)
print(language[0])
print(language[0].title())
print(language[-1].title())

language[0] = 'C'
language[1] = 'C++'
print(language)

language.append('python')
language.insert(0, 'PHP')
print(language)

del language[0]
language.pop(4)
language.remove('java')
print(language)

print(sorted(language))
print(sorted(language, reverse=True))

language.reverse()
print(language)

language.sort()
print(language)

language.sort(reverse=True)
print(language)

print(len(language))