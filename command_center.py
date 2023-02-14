list_of_integers = [int(x) for x in input().split()]

command = input()
while command != 'end':
    command_args = command.split()
    main_command = command_args[0]
    if main_command == 'swap':
        first_i, next_i = [int(x) for x in command_args[1:]]
        if not 0 <= first_i <= next_i < len(list_of_integers):
            continue
        list_of_integers[first_i], list[next_i] = list_of_integers[next_i], list_of_integers[first_i]
    elif main_command == 'enumerate_list':
        [print(f'[({i}, {v})]'.join([str(i, v) for i, v in enumerate(list_of_integers)])]
    elif main_command == 'max':
        pass
    elif main_command == 'min':
        pass
    elif main_command == 'get_divisible':
        pass
    command = input()