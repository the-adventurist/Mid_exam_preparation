waiting_people = int(input())
wagons = [int(x) for x in input().split()]

there_is_free_space_in_wagons = False
for wagon in range(len(wagons)):
    free_capacity = 4 - wagons[wagon]
    if waiting_people >= free_capacity:
        waiting_people -= free_capacity
        wagons[wagon] = 4
    else:
        free_capacity = waiting_people
        wagons[wagon] += free_capacity
        waiting_people = 0
        there_is_free_space_in_wagons = True
if there_is_free_space_in_wagons:
    print('The lift has empty spots!')
    print(' '.join([str(x) for x in wagons]))
elif waiting_people:
    print(f'There isn\'t enough space! {waiting_people} people in a queue!')
    print(' '.join([str(x) for x in wagons]))
else:
    print(' '.join([str(x) for x in wagons]))
