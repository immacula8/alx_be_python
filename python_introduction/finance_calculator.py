user_monthly_income = int(input('Enter your monthly income: '))
user_monthly_expenses = int(input('Enter your total monthly expenses: '))

user_monthly_savings = user_monthly_income - user_monthly_expenses

projected_savings = user_monthly_savings * 12 + (user_monthly_savings * 12 * 0.05)

print('Your monthly savings are $' + str(user_monthly_savings))
print('Projected savings after one year, with interest, is: $' + int(str(projected_savings)))
