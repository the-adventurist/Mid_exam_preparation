days = int(input())
plunder_per_day = int(input())
wanted_threshold = int(input())
gathered_plunder = 0

for day in range(1, days + 1):
    gathered_plunder += plunder_per_day
    if day % 3 == 0:
        gathered_plunder += 0.5 * plunder_per_day
    if day % 5 == 0:
        gathered_plunder *= 0.7

if gathered_plunder >= wanted_threshold:
    print(f'Ahoy! {gathered_plunder:.2f} plunder gained.')
else:
    gathered_plunder = gathered_plunder / wanted_threshold * 100
    print(f'Collected only {gathered_plunder:.2f}% of the plunder.')
    