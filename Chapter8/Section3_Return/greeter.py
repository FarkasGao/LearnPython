def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
    
# 这是一个无限循环
while True:
    print("\nPlease tell me your name:")
    print("(Enter 'quit' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'quit':
        break
    l_name = input("Last name: ")
    if l_name == 'quit':
        break
    
    format_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {format_name}")