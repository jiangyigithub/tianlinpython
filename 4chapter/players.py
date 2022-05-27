players=['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])#差一
print(players[2:])
print(players[-3:])


print("Here are the first three palyers on m team:")
for player in players[:3]:
    print(player.title())