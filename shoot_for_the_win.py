targets = [int(x) for x in input().split()]
index = input()
shoot_targets = 0

while index != 'End':
    index = int(index)
    if 0 <= index < len(targets):
        shooting_value = targets[index]
        targets[index] = -1
        shoot_targets += 1
        for current_target in range(len(targets)):
            if targets[current_target] == -1:
                continue
            if targets[current_target] > shooting_value:
                targets[current_target] -= shooting_value
            else:
                targets[current_target] += shooting_value
    index = input()
print(f'Shot targets: {shoot_targets} -> {" ".join(str(x) for x in targets)}')
