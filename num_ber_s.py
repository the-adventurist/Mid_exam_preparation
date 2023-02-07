numbers = sorted([int(x) for x in input().split()], reverse=True)
avr_number = sum(numbers) / len(numbers)
top_5 = []
count_numbers = 0
for num in numbers:
    if num > avr_number and count_numbers < 5:
        top_5.append(num)
        count_numbers += 1
if not top_5:
    print('No')
else:
    print(' '.join(str(x) for x in top_5))
