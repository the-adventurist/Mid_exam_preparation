incoming_list = input()
while incoming_list != 'stop playing':
    unique_numbers = True
    list_numbers = [int(x) for x in incoming_list.split()]
    result_list_of_numbers = []
    if len(list_numbers) == len(set(list_numbers)):
        result_list_of_numbers = [x + 2 if x % 2 == 0 else x for x in list_numbers]
    else:
        unique_numbers = False
        result_list_of_numbers = [x + 3 if x % 2 == 1 else x for x in list_numbers]
    output = sum(result_list_of_numbers) / len(result_list_of_numbers)
    if unique_numbers:
        print(f"Unique list: {','.join([str(x) for x in sorted(result_list_of_numbers)])}")
        print(f'Output: {output:.2f}')
    else:
        print(f"Non-unique list: {':'.join([str(x) for x in sorted(result_list_of_numbers)])}")
        print(f'Output: {output:.2f}')
    incoming_list = input()

