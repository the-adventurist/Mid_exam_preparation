elements = input().split()
chosen_indexes = input()

moves = 0
while chosen_indexes != 'end':
    moves += 1
    first_index, second_index = [int(x) for x in chosen_indexes.split()]
    if first_index == second_index or not(0 <= first_index < len(elements)) or not(0 <= second_index < len(elements)):
        elements.insert(len(elements) // 2, f'-{moves}a')
        elements.insert(len(elements) // 2, f'-{moves}a')
        print('Invalid input! Adding additional elements to the board')
        chosen_indexes = input()
        continue
    if elements[first_index] == elements[second_index]:
        element = elements[first_index]
        elements.remove(element)
        elements.remove(element)
        print(f"Congrats! You have found matching elements - {element}!")
        if not elements:
            print(f"You have won in {moves} turns!")
            break
    else:
        print("Try again!")
    chosen_indexes = input()
if elements:
    print('Sorry you lose :(')
    print(' '.join(elements))
