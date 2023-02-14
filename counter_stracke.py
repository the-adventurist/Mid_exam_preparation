energy = int(input())
won_battles = 0
distance = input()

insufficient_energy = False
while distance != 'End of battle':
    distance = int(distance)
    if energy < distance:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        insufficient_energy = True
        break
    won_battles += 1
    if won_battles % 3 == 0:
        energy += won_battles
    energy -= distance
    distance = input()
if not insufficient_energy:
    print(f"Won battles: {won_battles}. Energy left: {energy}")