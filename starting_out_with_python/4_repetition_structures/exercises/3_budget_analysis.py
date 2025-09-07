# Program to calculate a user's monthly spending and compare against their budget for the month.

def determine_budget() -> float:
    """Get the user's monthly budget."""
    monthly_budget = float(input('How much have you budgeted for this month?: '))

    # Input validation.
    while monthly_budget < 0:
        print("You cannot input a negative budget, please try again: ")
        monthly_budget = float(input())

    return monthly_budget

def get_expenses() -> list[float]:
    """Get the user's expenses for the month."""
    expenses = []
    i = 1
    while True:
        cost = float(input(f"Enter the cost of expense {i}: "))

        # Input validation.
        if cost <= 0:
            print("You cannot input a negative cost, please try again: ")
            cost = float(input())

        expenses.append(cost)

        # Determine if the user wants to insert another expense.
        go_again = input('Enter another expense (y/n)?: ')
        if go_again.lower() == 'n':
            break

    return expenses

def calculate_pnl(monthly_budget: float, expenses: list[float]) -> float:
    """Determine if the user overspent or was within budget."""
    return monthly_budget - sum(expenses)


def main():
    """Main function for determining if a user is over- or underbudget."""
    # Get the user's monthly budget
    budget = determine_budget()

    # Get the user's monthly expenses.
    expenses = get_expenses()

    # Determine if the user overspent or was within budget.
    pnl = calculate_pnl(budget, expenses)

    # Output
    print(f"\nMonthly budget: ${budget:.2f}")
    print(f"Monthly expenses: ${sum(expenses):.2f}")
    if pnl < 0:
        print(f"You are overbudget by ${abs(pnl - budget):.2f}")
    else:
        print(f"You are well-within budget by ${abs(pnl - budget):.2f}")


# Call the main function.
if __name__ == '__main__':
    main()