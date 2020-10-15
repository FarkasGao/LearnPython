available_toppings = ('mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese')
                      
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            if requested_topping == 'green peppers':
                print("Sorry, we are out of green peppers right now.")
            else:
                print(f"Adding {requested_topping}.")
        else:
            print(f"sorry, we don't have {requested_topping}.")
else:
    print("Are you sure you want a plain pizza")
print("\nFinished making your pizza!")