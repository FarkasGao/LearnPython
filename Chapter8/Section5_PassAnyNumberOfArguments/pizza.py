def make_pizza(size, *toppings):
    """打印顾客点的所有配料"""
    """概述要制作的披萨"""
    print(f"\nMaking a {size} inch pizza with the follwoing toppings:")
    for topping in toppings:
        print(f"-{topping}")
    
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')