

guests = ['ceej', 'beej', 'meej']

print(f"Welcome, {guests[0]}!")
print(f"Welcome, {guests[1]}!")
print(f"Welcome, {guests[2]}!")

l_guest = guests.pop()

print('\n',guests, "I am sorry, but ", l_guest, "cannot come")

guests.append('leej')
print(f"\nWelcome, {guests[0]}!")
print(f"Welcome, {guests[1]}!")
print(f"Welcome, {guests[2]}!")



guests.insert(0,'heej')
guests.insert(2, 'deej')
guests.append('xeej')

print('\n', guests)

print(f"\nWelcome, {guests[0]}!")
print(f"Welcome, {guests[1]}!")
print(f"Welcome, {guests[2]}!")
print(f"Welcome, {guests[3]}!")
print(f"Welcome, {guests[4]}!")
print(f"Welcome, {guests[5]}!")


print("\nonly two people can come", '\n',guests)

guests.pop()
print(guests)
guests.pop()
print(guests)
guests.pop()
print(guests)
guests.pop()
print(guests)

print("\nCongrat, you can come", guests[0])
print("Congrat, you can come", guests[1])


del guests[0]
print(guests)

del guests[0]
print(guests)

#ex siper







cars = ['bmw', 'audi', 'toyota', 'subaru']

print('\n\n\n\n\n\n\n\n\n\n\n\n',cars)

print('\n\n', 'Og List: ', cars)
print('\n\n', 'Sorted List: ', (sorted(cars)))
