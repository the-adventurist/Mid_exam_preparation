def forward_backward_command(p, s, addresses, d):
    if 0 <= p + s < len(house_addresses) and d == 'Forward':
        p += s
        del addresses[p]
        return p
    elif 0 <= p - s < len(house_addresses) and d == 'Back':
        p -= s
        del addresses[p]
        return p
    return p


number_of_commands = int(input())
house_addresses = [int(x) for x in input().split()]
command = input()
current_position = 0

while command:
    command_args = command.split()
    main_command = command_args[0]
    if main_command == 'Forward':
        steps = int(command_args[1])
        current_position = forward_backward_command(current_position, steps, house_addresses, main_command)
    elif main_command == 'Back':
        steps = int(command_args[1])
        current_position = forward_backward_command(current_position, steps, house_addresses, main_command)
    elif main_command == 'Gift':
        index = int(command_args[1])
        new_house_number = int(command_args[2])
        if 0 <= index < len(house_addresses):
            house_addresses.insert(index, new_house_number)
            current_position = index
    else:
        house_number1 = int(command_args[1])
        house_number2 = int(command_args[2])
        if house_number1 not in house_addresses or house_number2 not in house_addresses or\
            (house_number1 not in house_addresses and house_number2 not in house_addresses):
            try:
                command = input()
            except EOFError:
                break
            continue
        index1 = house_addresses.index(house_number1)
        index2 = house_addresses.index(house_number2)
        house_addresses[index1], house_addresses[index2] = house_addresses[index2], house_addresses[index1]
    try:
        command = input()
    except EOFError:
        break
print(f'Position: {current_position}')
print(', '.join([str(x) for x in house_addresses]))
