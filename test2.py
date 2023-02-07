new_list = [6, 8, 8]

max_num_odd = float('-inf')
searched_index = None
for i, m in enumerate(new_list):
    if m % 2 != 0 and m >= max_num_odd:
        max_num_odd = m
        searched_index = i
if not searched_index:
    print('no')
else:
    index_2 = new_list.index(max_num_odd)
    print(index_2)
    print(searched_index)