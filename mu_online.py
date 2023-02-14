health = 100
bitcoin = 0

current_room = 0
rooms = input().split('|')
you_re_dead = False
for i, room in enumerate(rooms):
    content, value = room.split()
    value = int(value)
    current_room += 1
    if content == 'potion':
        if value > 100 - health:
            value = 100 - health
        health += value
        print(f"You healed for {value} hp.")
        print(f"Current health: {health} hp.")
    elif content == 'chest':
        bitcoin += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if health:
            print(f"You slayed {content}.")
        else:
            print(f"You died! Killed by {content}.")
            you_re_dead = True
            break
if not you_re_dead:
    print(f"""You've made it!
Bitcoins: {bitcoin}
Health: {health}""")
else:
    print(f"Best room: {current_room}")
