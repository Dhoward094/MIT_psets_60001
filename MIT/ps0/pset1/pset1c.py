portion_down_payment = 0.25
r = 0.04

annual_salary = input("Enter your starting salary: ")
total_cost = 1000000
portion_saved = 0.5
annual_salary = float(annual_salary)
semi_annual_raise = 0.07

high = 1.0
low = 0


def calc(portion_saved):
    # does calculation for the number of months to save for a dream house
    current_savings = 0
    months = 0
    current_annual_salary = annual_salary

    while months <= 36:
        monthly_return = current_savings * r / 12
        monthly_savings = portion_saved * current_annual_salary / 12
        current_savings += monthly_return + monthly_savings
        months += 1

        if months % 6 == 0:
            current_annual_salary += round(current_annual_salary * semi_annual_raise, 2)

        elif months > 36:
            print("Not possible with current salary")
            exit(0)

    return current_savings


def guess():
    return round((high + low) / 2, 4)


num_guess = 1

while True:
    guessed_percent = guess()
    guess_savings = calc(guessed_percent)
    rounded_guess = round(guess_savings, 2)

    if rounded_guess < 249900:
        low = guessed_percent

    elif rounded_guess > 250100:
        high = guessed_percent
    else:
        break

    num_guess += 1

best_savings_rate = guessed_percent
print(f"Best savings rate: {best_savings_rate}")
print(f"Steps in bisection search: {num_guess}")