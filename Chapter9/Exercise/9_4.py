class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"My restaurant name is {self.restaurant_name}.")
        print(f"And We have the following dishes:")
        print(f"-{self.restaurant_name} -{self.cuisine_type}")
        
    def status(self):
        print("Restaurant is open now")
        
    def customer(self, number):
        """将将就餐人数增加指定的量"""
        if number >= 0:
            self.number_served += number
            
    def customer_number(self):
        """打印总就餐人数"""
        print(f"A total of {self.number_served} people come here for dinner")
        
restaurant = Restaurant("This is a restaurant in Michelin Red Guide", "exerything")

print(f"{restaurant.restaurant_name}")
print(f"There have {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.status()

restaurant.customer_number()
restaurant.customer(10)
restaurant.customer_number()