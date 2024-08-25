
h = input("How tall cm?")
h = int(h)

if h >= 130:
    print("\nYou can")
else:
    print("\nYou can't")



nr = int(input("Enter nr and i tell + or -: "))


if nr % 2 == 0:
    print(f"\nNr {nr} is +")
else:
    print(f"\nNr {nr} is -")



cars = ['bmw', 'audi', 'benz']

car = input("what car you like?\n")

print("\nLet me see if i have...")

if car in cars:
    print(f"\nWe have {car}")
else:
    print(f"\nWe have not {car}")



guest_nr = int(input("How many people eating? (nr)"))

if guest_nr <= 8:
    print("Welcome, table is ready")
else:
    print("You wait until table is ready")




nr = int(input("I tell if nr is multiple of 10 (nr)\n"))

if nr % 10 == 0:
    print(f"Yes {nr} is multiple of 10")
else:
    print(f"No {nr} is not multiple of 10")

