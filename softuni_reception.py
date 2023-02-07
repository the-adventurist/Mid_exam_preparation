first_employee_efficient = int(input())
second_employee_efficient = int(input())
third_employee_efficient = int(input())
the_whole_efficient = first_employee_efficient + second_employee_efficient + third_employee_efficient
students = int(input())
needed_hours = 0

while students:
    needed_hours += 1
    if needed_hours % 4 == 0:
        continue
    students -= the_whole_efficient
    if students <= 0:
        break

print(f'Time needed: {needed_hours}h.')

