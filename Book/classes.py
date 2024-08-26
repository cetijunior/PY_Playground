class Dog:
    '''simple dog model'''
    def __init__(self, name, age):
        '''init name and age attributes'''
        self.name = name
        self.age = age

    def sit(self):
        '''Simulta dog sitting in response to a command'''
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        '''Simulta dog rolling over in response to a command'''
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.roll_over()




class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThe restaurant is called: '{self.restaurant_name}'")
        print(f"'{self.restaurant_name}'s cuisine is: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\n\tThe restaurant: '{self.restaurant_name}' is now open!")

new_restaurant1 = Restaurant('The CJ', "Albanian")
new_restaurant1.describe_restaurant()
new_restaurant1.open_restaurant()

new_restaurant2 = Restaurant('Amorte', "Alien")
new_restaurant2.describe_restaurant()
new_restaurant2.open_restaurant()

new_restaurant3 = Restaurant('Unmortricken', "Medetiterreian")
new_restaurant3.describe_restaurant()
new_restaurant3.open_restaurant()



class User:
    def __init__(self, first_name, last_name, age, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self.height = height
        self.weight = weight

    def describe_user(self):
        if self.age >= 18:
            print(f"\nSoldier: \n\t- {self.first_name} {self.last_name}\n\t- age: {self.age}\n\t- height: {self.height}\n\t- weight: {self.weight}\n\t- is ready to report for duty!")
        else:
            print(f"\nSoldier: \n\t- {self.first_name} {self.last_name}\n\t- age: {self.age}\n\t- height: {self.height}\n\t- weight: {self.weight}\n\t- is not ready to report for duty!")
            print("You are too young to serve your Country Soldier")

    def greet_user(self):
        f_name = f"{self.first_name} {self.last_name}"
        if self.age >= 18:
            print(f"\nHello {f_name}!\nThe sacrifice you are about to make for your country will make you part of our history forever Soldier. May god be with You")
        else:
            print("\nWe appriciate your eagerness Soldier, come back when you are older.")


user1 = User('CJ', "Lame", "21", '177', '74')
user1.describe_user()
user1.greet_user()


user2 = User('BJ', "Bame", "20", '174', '71')
user2.describe_user()
user2.greet_user()

user3 = User('DJ', "Dame", "17", '172', '68')
user3.describe_user()
user3.greet_user()
