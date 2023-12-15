

portion_down_payment = 0.25
r = 0.04

annual_salary = input("Enter your annual salary: ")
portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
total_cost = input("Enter the cost of your dream home: ")
semi_annual_raise = input("Enter the percentage of your semi-annual raise, as a decimal: ")

annual_salary = float(annual_salary)
portion_saved = float(portion_saved)
total_cost = float(total_cost)
semi_annual_raise = float(semi_annual_raise)


def calc():
    # does calculation for the number of months to save for a dream house
    down_payment = total_cost * portion_down_payment
    current_savings = 0
    months = 0
    current_annual_salary = annual_salary

    while current_savings < down_payment:
        monthly_return = current_savings * r / 12
        monthly_savings = portion_saved * current_annual_salary / 12
        current_savings += monthly_return + monthly_savings
        months += 1

        if months % 6 == 0:
            current_annual_salary += current_annual_salary * semi_annual_raise

    return months


months_to_save = calc()
print(f"Number of months: {months_to_save}")