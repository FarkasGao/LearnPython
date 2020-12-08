age=-1
def t1():
     age=-1
     while age <= 0:
             try:
                     age = int(input("Enter your age in years: "))
                     if age < 0:
                             print('Your age must be positive')
             except ValueError:
                     print("There was an unexpected error reading input.")
             except EOFError:
                     print("There was an unexpected error reading input.")
                     raise
t1()