pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
    
print(f"you ordered a {pizza['crust']}-crust pizza"
    "with the follow toppings:")
        
for topping in pizza['toppings']:
    print("\t" + topping)