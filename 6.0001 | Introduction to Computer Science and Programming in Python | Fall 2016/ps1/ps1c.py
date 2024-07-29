# User inputs

annual_salary_input = float(input('Enter your starting annual salary: '))


# Constants

portion_down_payment = 0.25
semi_annual_raise = .07
total_cost = 1_000_000
r = 0.04


# Counters

portion_saved_left = 0
portion_saved_right = 10000
portion_saved = (portion_saved_left + portion_saved_right) // 2
epsilon = 100
steps = 0
possible = True


# Program

while True:
    if annual_salary_input * 3 < total_cost * portion_down_payment:
        possible = False
        print('It is not possible to pay the down payment in three years.')
        break
    current_savings = 0
    months = 0
    annual_salary = annual_salary_input
    monthly_salary = annual_salary / 12
    steps = steps + 1
    while months < 36:
        current_savings = current_savings + (monthly_salary * (portion_saved / 10000))
        current_savings = current_savings + ((current_savings * r) / 12)
        months = months + 1
        if (months + 1) % 6 == 0:
            monthly_salary = monthly_salary * (1 + semi_annual_raise)
    if abs(current_savings - portion_down_payment * total_cost) <= 100:
        break
    else:
        if current_savings > portion_down_payment * total_cost:
            portion_saved_right = portion_saved
        else:
            portion_saved_left = portion_saved
    portion_saved = (portion_saved_left + portion_saved_right) // 2



# Output
if possible:
    print('Best savings rate:', portion_saved / 10000)
    print('Steps in bisection search:', steps)
