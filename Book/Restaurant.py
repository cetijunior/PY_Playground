class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.customers_served = 0

    def describe_restaurant(self):
        print(f"\nThe restaurant is called: '{self.restaurant_name}'")
        print(f"'{self.restaurant_name}'s cuisine is: {self.cuisine_type}")
        print(f"'{self.restaurant_name}' has served: {self.customers_served} customers")

    def open_restaurant(self):
        print(f"\n\t --- The restaurant: '{self.restaurant_name}' is now open! ---")

    def set_number_served(self, clients):
        if clients >= self.customers_served:
            self.customers_served = clients
        else:
            print("You cannot un-serve customers")

    def increment_nr_served(self, customers):
        self.customers_served += customers
        print(f"\t- '{self.restaurant_name}' has now served: {self.customers_served} customers")



new_restaurant1 = Restaurant('The CJ', "Albanian")
new_restaurant1.open_restaurant()
new_restaurant1.describe_restaurant()

new_restaurant2 = Restaurant('Amorte', "Alien")
new_restaurant2.open_restaurant()
new_restaurant2.set_number_served(12)
new_restaurant2.describe_restaurant()

new_restaurant3 = Restaurant('Unmortricken', "Medetiterreian")
new_restaurant3.open_restaurant()
new_restaurant3.set_number_served(14)
new_restaurant3.describe_restaurant()
new_restaurant3.increment_nr_served(14)



class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'caramel', 'vanilla', 'cookies']

    def show_flavors(self):
        print(f"{self.restaurant_name} has these flavors: ")
        for flavor in self.flavors:
            print(f"\t- {flavor.title()}")


new_Ice = IceCreamStand('Akulli', 'Ice Cream')
new_Ice.open_restaurant()
new_Ice.describe_restaurant()
new_Ice.show_flavors()
new_Ice.increment_nr_served(14)

