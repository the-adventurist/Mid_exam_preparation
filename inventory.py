inventory = input().split(', ')

command = input()
while command != 'Craft!':
    command_args = command.split(' - ')
    main_command = command_args[0]
    if main_command == 'Collect':
        item = command_args[1]
        if item not in inventory:
            inventory.append(item)
    elif main_command == 'Drop':
        item = command_args[1]
        if item in inventory:
            inventory.remove(item)
    elif main_command == 'Combine Items':
        old_item, new_item = command_args[1].split(":")
        if old_item in inventory:
            index = inventory.index(old_item)
            inventory.insert(index + 1, new_item)
    else:
        item = command_args[1]
        if item in inventory:
            inventory.append(inventory.pop(inventory.index(item)))

    command = input()

print(', '.join(inventory))
