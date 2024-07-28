# User inputs

annual_salary = float(input('Enter your starting annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi­annual raise, as a decimal: '))


# Constants

portion_down_payment = 0.25
monthly_salary = annual_salary / 12
r = 0.04


# Counters

current_savings = 0
months = 0


# Program

while current_savings < total_cost * portion_down_payment:
    current_savings = current_savings + (monthly_salary * portion_saved)
    current_savings = current_savings + ((current_savings * r) / 12)
    months = months + 1
    if (months + 1) % 6 == 0:
        monthly_salary = monthly_salary * (1 + semi_annual_raise)


# Output
print('Number of months:', months)
