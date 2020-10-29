def make_car(manufacturer, model, **attribute):
    attribute[manufacturer] = manufacturer
    attribute[model] = model
    return attribute
    
car = make_car('subaru', 'outback', color = 'blue', tow_package = True)

print(car)