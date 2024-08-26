from multiprocessing.connection import answer_challenge

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


age = 20
if age >=18:
    print("\n\nyou can vote")
    print("have you vote?")
else:
    print("\n\nyou cant vote")
    print("come back 18")