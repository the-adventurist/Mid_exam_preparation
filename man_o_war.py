pirate_ship = [int(x) for x in input().split('>')]
war_ship = [int(x) for x in input().split('>')]
maximum_health_capacity = int(input())

command = input()
no_stalemate = True
while command != 'Retire':
    command_args = command.split()
    main_command = command_args[0]
    if main_command == 'Fire':
        index, damage = [int(x) for x in command_args[1:]]
        if 0 <= index < len(war_ship):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                no_stalemate = False
                break
    elif main_command == 'Defend':
        start_i, end_i, damage = [int(x) for x in command_args[1:]]
        if 0 <= start_i <= end_i < len(pirate_ship):
            for target in range(start_i, end_i + 1):
                pirate_ship[target] -= damage
                if pirate_ship[target] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    no_stalemate = False
                    break
    elif main_command == 'Repair':
        index, health = [int(x) for x in command_args[1:]]
        if 0 <= index < len(pirate_ship):
            if health > maximum_health_capacity - pirate_ship[index]:
                health = maximum_health_capacity - pirate_ship[index]
            pirate_ship[index] += health
    elif main_command == 'Status':
        count = [+1 for x in pirate_ship if x < 0.2 * maximum_health_capacity]
        print(f"{len(count)} sections need repair.")
    command = input()
if no_stalemate:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
