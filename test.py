int_list = [int(x) for x in input().split()]

new_list = int_list

while True:
    command = input()
    if command == 'end':
        break
    command = command.split()

    if command[0] == 'exchange':
        if int(command[1]) >= len(new_list) or int(command[1]) < 0:
            print('Invalid index')
        else:
            first_half = new_list[0:int(command[1]) + 1]
            second_half = new_list[int(command[1]) + 1:]
            new_list = second_half + first_half

    elif command[0] == 'max':
        if command[1] == 'even':
            max_num_even = float('-inf')
            searched_index = None
            for i, l in enumerate(new_list):
                if l % 2 == 0 and l >= max_num_even:
                    max_num_even = l
                    searched_index = i
            if max_num_even == float('-inf'):
                print('No matches')
            else:
                print(searched_index)
        elif command[1] == 'odd':
            max_num_odd = float('-inf')
            searched_index = None
            for i, m in enumerate(new_list):
                if m % 2 != 0 and m >= max_num_odd:
                    max_num_odd = m
                    searched_index = i
            if max_num_odd == float('-inf'):
                print('No matches')
            else:
                print(searched_index)
    elif command[0] == 'min':
        if command[1] == 'even':
            min_num_even = float('inf')
            searched_index = None
            for i, n in enumerate(new_list):
                if n % 2 == 0 and n <= min_num_even:
                    min_num_even = n
                    searched_index = i
            if min_num_even == float('inf'):
                print('No matches')
            else:
                print(searched_index)
        elif command[1] == 'odd':
            min_num_odd = float('inf')
            searched_index = None
            for i, o in enumerate(new_list):
                if o % 2 != 0 and o <= min_num_odd:
                    min_num_odd = o
                    searched_index = i
            if min_num_odd == float('inf'):
                print('No matches')
            else:
                print(searched_index)

    elif command[0] == 'first':
        if command[2] == 'even':
            command_1 = int(command[1])
            if command_1 >= len(new_list) or command_1 < 0:
                print('Invalid count')
                continue
            first_even = []
            counter = 0
            for p in new_list:
                if counter == command_1:
                    break
                elif p % 2 == 0:
                    first_even.append(p)
                    counter += 1
            print(first_even)
        elif command[2] == 'odd':
            command_1 = int(command[1])
            if command_1 >= len(new_list) or command_1 < 0:
                print('Invalid count')
                continue
            first_odd = []
            counter = 0
            for q in new_list:
                if counter == command_1:
                    break
                elif q % 2 != 0:
                    first_odd.append(q)
                    counter += 1
            print(first_odd)

    elif command[0] == 'last':
        if command[2] == 'even':
            command_1 = int(command[1])
            if command_1 >= len(new_list) or command_1 < 0:
                print('Invalid count')
                continue
            last_even = []
            counter = 0
            new_list_reversed = reversed(new_list)
            for r in new_list_reversed:
                if counter == command_1:
                    break
                elif r % 2 == 0:
                    last_even.append(r)
                    counter += 1
            last_even = list(reversed(last_even))
            print(last_even)
        elif command[2] == 'odd':
            command_1 = int(command[1])
            if command_1 >= len(new_list) or command_1 < 0:
                print('Invalid count')
                continue
            last_odd = []
            counter = 0
            new_list_reversed = reversed(new_list)
            for s in new_list_reversed:
                if counter == command_1:
                    break
                elif s % 2 != 0:
                    last_odd.append(s)
                    counter += 1
            last_odd = list(reversed(last_odd))
            print(last_odd)

print(new_list)
