class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"My restaurant name is {self.restaurant_name}.")
        print(f"And We have the following dishes:")
        print(f"-{self.restaurant_name} -{self.cuisine_type}")
        
    def status(self):
        print("Restaurant is open now")
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['a', 'b', 'c']
    def ice_cream_flavors(self):
        print(self.flavors)
        
restaurant = Restaurant("This is a restaurant in Michelin Red Guide", "exerything")

print(f"{restaurant.restaurant_name}")
print(f"There have {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.status()

ice = IceCreamStand("AAA", "sss")
ice.ice_cream_flavors()
ice.describe_restaurant()