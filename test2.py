current_room = 0
best_room = 0
room_value = 0
health = 100
bitcoins = 0
you_are_killed = False
dungeon_s_room = input().split('|')
for room in dungeon_s_room:
    thing, value = room.split()
    value = int(value)
    current_room += 1
    if thing == 'potion':
        if 100 - health < value:
            value = 100 - health
        health += value
        print(f"You healed for {value} hp.")
        print(f"Current health: {health} hp.")
    elif thing == 'chest':
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if health > 0:
            print(f"You slayed {thing}.")
        else:
            print(f"You died! Killed by {thing}.")
            you_are_killed = True
            break
if you_are_killed:
    print(f"Best room: {current_room}")
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
