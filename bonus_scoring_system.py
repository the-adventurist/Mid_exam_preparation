from math import ceil

students = int(input())
lectures_number = int(input())
additional_bonus = int(input())
max_bonus_points = 0
students_best_attendance = 0

for _ in range(students):
    student_attendance = int(input())
    current_bonus = student_attendance / lectures_number * (5 + additional_bonus)
    if max_bonus_points < current_bonus:
        max_bonus_points = current_bonus
        students_best_attendance = student_attendance

print(f'Max Bonus: {ceil(max_bonus_points)}.')
print(f'The student has attended {students_best_attendance} lectures.')
