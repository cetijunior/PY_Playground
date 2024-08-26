'''
def fav_book(book, username):
    print(f"\n{username}'s favorite book is {book}")

username = input('Insert name here:\n')
book = input("enter fav book: \n")

fav_book(book, username)



from itertools import repeat

pets = {}
poll = True

def describe_pet(animal_type, pet_name):
    for animal_type, pet_name in pets.items():
        print(f"\nI have a {animal_type}.")
        print(f"My {animal_type}'s name is {pet_name.title()}")


while poll:
    animal_type: str = str(input('Insert animal type:\n'))
    pet_name: str = str(input("Insert Pet Name:\n"))

    pets[animal_type]=pet_name

    repeat = animal_type = input("want to add other animal?\n")
    if repeat == 'no':
        poll = False


describe_pet(animal_type, pet_name)


'''
from itertools import repeat

shirts = {}
order = True


def make_shirt(size, message):
    for size, message in shirts.items():
        print(f"\nMaking shirt:  \n\t- size: {size}\n\t- message: {message}.")


while order:
    size= input("enter shirt size: \n")
    if size == '':
        size = 'large'

    message = input("enter message: \n")
    if message == '':
        message = 'i love python'

    shirts[size] = message

    repeat = input("Want to make another shirt (no)\n")
    if repeat == 'no':
        order = False

make_shirt(size, message)
