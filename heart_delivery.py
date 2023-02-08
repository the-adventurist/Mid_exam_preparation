neighborhood = [int(x) for x in input().split('@')]

cupid_current_position = 0
while True:
    jump = input()
    if jump == 'Love!':
        break
    jump_args = jump.split()
    jump_length = jump_args[1]
    jump_length = int(jump_length)
    landed = jump_length + cupid_current_position
    if landed >= len(neighborhood):
        landed = 0
    cupid_current_position = landed
    if neighborhood[landed] == 0:
        print(f"Place {landed} already had Valentine's day.")
    elif neighborhood[landed] > 0:
        neighborhood[landed] -= 2
        if neighborhood[landed] == 0:
            print(f"Place {landed} has Valentine's day.")

print(f"Cupid's last position was {cupid_current_position}.")
no_celebrated_houses = [+1 for x in neighborhood if x != 0]
if not no_celebrated_houses:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(no_celebrated_houses)} places.")
