input_str = input().split()

while True:
    new_string = ""
    command = input()
    if command == "3:1":
        break

    current_input = command.split()
    action = current_input[0]
    first = int(current_input[1])
    last = int(current_input[2])



    if action == "merge":
        if first < 0:
            first = 0
        if last >= len(input_str):
            last = len(input_str) - 1
        if not 0 <= first < last < len(input_str):
            continue
        for i in range(first, last + 1):
            new_string += input_str[i]
        del input_str[first: last + 1]
        input_str.insert(first, new_string)
    elif action == "divide":
        temp_list1 = [[] for i in range(last)]
        chunk = (len(input_str[first]) // last)
        a = 0
        b = chunk
        for i in range(last):
            if i < last - 1:
                temp_list1[i].append(input_str[first][a:b])
                a += chunk
                b += chunk
            else:
                temp_list1[i].append(input_str[first][a:])
        input_str.pop(first)
        for i in range(len(temp_list1) - 1, -1, -1):
            input_str.insert(first, temp_list1[i][0])
print(' '.join(input_str))
