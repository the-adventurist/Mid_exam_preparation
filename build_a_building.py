project_budget = float(input())
initial_capital = float(input())
numbers_of_investors = int(input())
number_investor = 0

for _ in range(numbers_of_investors):
    investment = 0
    if initial_capital < project_budget:
        investment = float(input())
        initial_capital += investment
        number_investor += 1
        print(f'Investor {number_investor} gave us {investment:.2f}.')
    else:
        break
if project_budget <= initial_capital:
    print(f'We will manage to build it. Start now! Extra money - {initial_capital - project_budget:.2f}.')
else:
    print(f'Project can not start. We need {project_budget - initial_capital:.2f} more.')
