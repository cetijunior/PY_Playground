
players = ['charl', 'mart', 'micha', 'flore', 'eli']

print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])




print("\n\n\nFirst players: ")
for player in players[:3]:
    print(player.title())



mine = ['cha', 'ma', 'li']
friends = mine[:]

print("\n\n\nMy foo:")
mine.append('ki')
print(mine)

print("My friend foo:")
friends.append('mi')
print(friends, '\n\n\n')


foods = ("buk", "Sup", "Patat", "Gjell", "Tort")
print("\nOG Tuple:")
for food in foods:
    print(food)

foods = ("buk", "Sup", "Patat", "Mish", "Tzazik")
print("\nMod Tuple:")
for food in foods:
    print(food)