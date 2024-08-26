'''
#Start with users that need to be verified
# and an empty list to hold the verified users

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#verify all users
#move verified to correct list

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Veryfing user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThese users have been verified: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())




pets = ['dog', 'duck', 'cat', 'dog', 'bill']
print(pets)

while 'dog' in pets:
    pets.remove('dog')

print(pets)



from itertools import repeat

responses = {}

#Flag to indicate the polling is active
poll_active = True

while poll_active:
    name = input("\nWhat is name?\n")
    response = input("what car you like? \n")

    #store response in dictionary
    responses[name] = response

    repeat = name = input("\nOther person to respond? (enter = yes | 'no' to end)\n")
    if repeat == 'no':
        poll_active = False

print("\n--- Poll Results ---\n")
for name, response in responses.items():
    print(f"{name} likes {response}")


from os import remove

sammich_orders = ['egg sammich', 'pastrami sammich', 'bologna sammich', 'pastrami sammich', 'tuna sammich', 'pastrami sammich']
finished_sammich = []

print("\t*There is no more pastrami sammich\n")

while sammich_orders:
    while 'pastrami sammich' in sammich_orders:
        sammich_orders.remove('pastrami sammich')
    done_sammich = sammich_orders.pop()
    print(f"- Making {done_sammich}")
    finished_sammich.append(done_sammich)

print("\n All sammich has ben made")


'''
from itertools import repeat

responses = {}
poll_active = True

while poll_active:
    name = input("What is name?\n")
    response = input("If you had one super power what would it be?\n")

    responses[name] = response

    repeat = name = input("Other answer?(no)\n")
    if repeat == 'no':
        poll_active = False

print("\t--- Poll Results ---\n")
for name, response in responses.items():
    print(f"- {name} wants {response}")