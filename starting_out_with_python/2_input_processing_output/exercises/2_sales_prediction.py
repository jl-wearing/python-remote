# Program to calculate the profit of a company.
PROFIT_PERCENTAGE = 0.23

# Input the sales amount.
sales_amount = float(input('Enter sales amount: '))

# Process profit as sales multiplied by profit percentage.
profit = sales_amount * PROFIT_PERCENTAGE

# Output the projected profit.
print(f"Projected Profit: ${profit:,.2f}")