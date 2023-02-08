groceries = input().split('!')

note = input()
while note != 'Go Shopping!':
    note_args = note.split()
    action = note_args[0]
    if action == 'Urgent':
        item = note_args[1]
        if item not in groceries:
            groceries.insert(0, item)
    elif action == 'Unnecessary':
        item = note_args[1]
        if item in groceries:
            groceries.remove(item)
    elif action == 'Correct':
        old_item = note_args[1]
        new_item = note_args[2]
        if old_item in groceries:
            i_old_item = groceries.index(old_item)
            groceries.insert(i_old_item, new_item)
            groceries.remove(old_item)
    else:
        item = note_args[1]
        if item in groceries:
            i_item = groceries.index(item)
            item = groceries.pop(i_item)
            groceries.append(item)
    note = input()
print(', '.join(groceries))
