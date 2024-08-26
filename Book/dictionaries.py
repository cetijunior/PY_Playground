'''
alien = {'color': 'green', 'points': 5}

print(f"alien is {alien['color']}")

alien['xP'] = 0
alien['yP'] = 25
alien['color'] = 'blue'


print(f"alien is now {alien['color']}")




print(alien['color'])
print(alien['points'])


newP = alien['points']
print(f"\n\nYou won {newP} points!")



alien = {'xP': 0, 'yP': 25, 'speed': 'medium'}
print(f"OG Position: {alien['xP']}")

if alien['speed'] == 'slow':
    xI = 1
elif alien['speed'] == 'medium':
    xI = 2
else:
    xI = 3

alien['xP'] = alien['xP'] + xI

print(f"New position : {alien['xP']}")
print(alien)

del alien['speed']
print(alien)



fav_lang = {
    'cj': 'java',
    'bj': 'bava',
    'dj': 'dava'
}

for name, lang in fav_lang.items():
    print(f"\nName: {name.upper()}")
    print(f"Lang: {lang.title()}\n")

for name in fav_lang.keys():
    print(name.title())

#lang = fav_lang['cj'].upper()
#print(f"CJ fav lang is {lang}")
'''



users = {
    "aeinstein": {
        'f': 'albert',
        'l': 'einstein',
        'loc': 'princeton',
    },
    "mcurie": {
        'f': 'marie',
        'l': 'curie',
        'loc': 'paris',
    },

}

for username, user_info in users.items():
    print(f"Username: {username}")
    fName = f"{user_info['f']} {user_info['l']}"
    location = user_info['loc']

    print(f"\tFull Name: {fName.title()}")
    print(f"\tLocation: {location.title()}")