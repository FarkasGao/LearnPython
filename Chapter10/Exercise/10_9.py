def cats_and_dogs(filename):
    """打印文件"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
        #print(f"Sorry, the file {filename} does not exist")
    else:
        print(contents)
        
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:  
    cats_and_dogs(filename)