songs = ["ROCKSTAR", "Do It", "For The Night"]


print(songs[0:3])

songs[0] = 'Never Gonna Give You Up'




songs.extend(["Happy", "New York", "Amadelle With Love"])
print(songs)

songs.pop(1)


animals = ['Iguana', 'Wolf', 'Polar Bear']
animals.append('Deer')
print(animals[2])
del animals[0]

for i in range(len(animals)):
    print(animals[i])