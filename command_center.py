list_of_integers = [int(x) for x in input().split()]

counter_of_valid_performed_commands = 0
command = input()
while command != 'end':
    command_args = command.split()
    main_command = command_args[0]
    if main_command == 'swap':
        first_i, next_i = [int(x) for x in command_args[1:]]
        if not 0 <= first_i < len(list_of_integers) or not 0 <= next_i < len(list_of_integers):
            print(list_of_integers)
            counter_of_valid_performed_commands += 1
            command = input()
            continue
        list_of_integers[first_i], list_of_integers[next_i] = list_of_integers[next_i], list_of_integers[first_i]
        print(list_of_integers)
        counter_of_valid_performed_commands += 1
    elif main_command == 'enumerate_list':
        tuples_data_lists_element = ''
        for i, v in enumerate(list_of_integers):
            if i == 0:
                tuples_data_lists_element += f'[({i}, {v}), '
            elif 0 < i < len(list_of_integers) - 1:
                tuples_data_lists_element += f'({i}, {v}), '
            else:
                tuples_data_lists_element += f'({i}, {v})]'
        print(tuples_data_lists_element)
        counter_of_valid_performed_commands += 1
    elif main_command == 'max':
        print(max(list_of_integers))
        counter_of_valid_performed_commands += 1
    elif main_command == 'min':
        print(min(list_of_integers))
        counter_of_valid_performed_commands += 1
    elif main_command == 'get_divisible':
        divisor = int(command_args[-1])
        result_list = [x for x in list_of_integers if x % divisor == 0]
        print(result_list)
        counter_of_valid_performed_commands += 1
    command = input()
print(counter_of_valid_performed_commands)
