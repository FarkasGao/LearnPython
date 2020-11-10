def get_formatted_name(first, last):
    """生成整洁的名字"""
    full_name = f"{first} {last}"
    return full_name.title()
    
def get_formatted_name2(first, middle, last):
    """生成整洁的名字"""
    full_name2 = f"{first} {middle} {last}"
    return full_name2.title()
    
def get_formatted_name3(first, last, middle=''):
    """生成整洁的名字"""
    if middle:
        full_name3 = f"{first} {middle} {last}"
    else:
        full_name3 = f"{first} {last}"
    return full_name3.title()