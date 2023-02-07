array_ = [int(x) for x in input().split()]

action = input()
while action != 'end':
    action_args = action.split()
    main_action = action_args[0]
    if main_action == 'swap':
        first_index = int(action_args[1])
        second_index = int(action_args[2])
        array_[first_index], array_[second_index] = array_[second_index], array_[first_index]
    elif main_action == 'multiply':
        first_index = int(action_args[1])
        second_index = int(action_args[2])
        array_[first_index] = array_[first_index] * array_[second_index]
    else:
        array_ = [x - 1 for x in array_]
    action = input()

print(', '.join(str(x) for x in array_))
