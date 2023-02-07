list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 78, 99, 102, 47, 89, 91]
number = list_[9]
for n in list_:
    if n <= number:
        n += number
        print(n, number)
    else:
        n -= number
        print(n, number)
list_[9] = 34
print(number)
list_copy = list_
list_copy[9] = 45
print(list_)
print(list_[9])
print(list_copy)
