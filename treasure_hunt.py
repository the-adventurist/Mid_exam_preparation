chest = input().split('|')

command = input()

while command != 'Yohoho!':
    command_args = command.split()
    main_command = command_args[0]
    if main_command == 'Loot':
        for element in command_args[1:]:
            if element not in chest:
                chest.insert(0, element)
    elif main_command == 'Drop':
        index = int(command_args[1])
        if 0 <= index < len(chest):
            chest.append(chest.pop(index))
    else:
        count = int(command_args[1])
        stolen_items = []
        for _ in range(count):
            if len(chest) > 0:
                stolen_item = chest.pop()
                stolen_items.append(stolen_item)
        print(', '.join(reversed(stolen_items)))
    command = input()


if chest:
    length_treasure_items = sum([len(x) for x in chest])
    avr_treasure_gain = length_treasure_items / len(chest)
    print(f'Average treasure gain: {avr_treasure_gain:.2f} pirate credits.')
else:
    print('Failed treasure hunt.')
