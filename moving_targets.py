def index_validator(i, targets_):
    if 0 <= i < len(targets_):
        return i


targets = [int(x) for x in input().split()]

action = input()
while action != 'End':
    action_args = action.split()
    main_action, index = action_args[0:2]
    index = int(index)
    if main_action == 'Shoot':
        index = index_validator(index, targets)
        if not index:
            action = input()
            continue
        power = int(action_args[2])
        targets[index] -= power
        if targets[index] <= 0:
            del targets[index]
    elif main_action == 'Add':
        index = index_validator(index, targets)
        if not index:
            action = input()
            print("Invalid placement!")
            continue
        value = int(action_args[2])
        targets.insert(index, value)
    else:
        radius = int(action_args[2])
        if 0 <= index - radius and index + radius < len(targets):
            first_part_targets = targets[: index - radius]
            second_part_targets = targets[index + radius + 1:]
            targets = first_part_targets + second_part_targets
        else:
            print("Strike missed!")
    action = input()
print('|'.join([str(x) for x in targets]))
