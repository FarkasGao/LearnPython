def describe_pet(pet_name, animal_type = 'cat'tractr):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('harry', 'hamster')
describe_pet('willie', 'dog')
describe_pet('david')
describe_pet('julia')