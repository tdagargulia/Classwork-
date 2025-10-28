class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")



restaurant1 = Restaurant("Leo Doro", "Italian")
restaurant2 = Restaurant("Sakura", "Japanese")
restaurant3 = Restaurant("Shemoikhede Genatsvale", "Georgian")


print(f"The restaurant1 name is {restaurant1.restaurant_name}.")
print(f"The restaurant1 cuisine type is {restaurant1.cuisine_type}.\n")

print(f"The restaurant2 name is {restaurant2.restaurant_name}.")
print(f"The restaurant2 cuisine type is {restaurant2.cuisine_type}.\n")

print(f"The restaurant3 name is {restaurant3.restaurant_name}.")
print(f"The restaurant3 cuisine type is {restaurant3.cuisine_type}.\n")


restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
