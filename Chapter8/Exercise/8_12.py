def sandwich(*args):
    print("making a sandwich with the following toppings")
    for arg in args:
        print(f"-{arg}")
        
sandwich('aaa', 'bbb', 'ccc')
sandwich('ddd', 'eee')
sandwich('fff')