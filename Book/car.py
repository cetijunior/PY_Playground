class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = int(year)
        self.odometer_reading = 0

    def get_descriptive_name(self):

        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):

        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll it back homie")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car('BMW', 'M4', 2022)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(18)
my_new_car.read_odometer()

my_old_car = Car('subaru', 'f30', 2012)
print(my_old_car.get_descriptive_name())
my_old_car.update_odometer(23_500)
my_old_car.read_odometer()
my_old_car.increment_odometer(100)
my_old_car.read_odometer()



class Battery:
    def __init__(self,battery_capacity = 89, battery_size=75):
        self.battery_size = battery_size
        self.battery_capacity = battery_capacity


    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")


    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
        print(f"This car's battery has a capacity of  {self.battery_capacity}%")

    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_capacity = 100
        elif self.battery_size ==100:
            self.battery_capacity = 100


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """ init attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


