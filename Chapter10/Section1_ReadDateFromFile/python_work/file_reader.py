with open('text_files\pi_digits.txt') as file_object:
#直接写在open中的\不会被误认为转义字符
    contents = file_object.read()
    print(file_object.read())
print(contents)

file_path = r'c:\users\25287\desktop\study\python\chapter10\section1_readdatefromfile\pi_digits2.txt'
#此处 "\" 会被理解成转义的意思，可以在"前加 "r" 保持字符串原有意思
#或者使用 "\\" , 或者使用 "/" 来代替  "\"
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)

filename = 'text_files\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in file_object:
        print(line.rstrip())
     
print("---------------")    
for line in lines:
    print(line.rstrip())
    
print(lines)