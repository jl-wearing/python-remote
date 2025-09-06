# Program to calculate the amount of money accrued after a specified number of years.
# A = P * (1+ (r/n)) ** (n * t), where
# A is the amount of money in the account after the specified number of years.
# P is the principal amount that was originally deposited into the account.
# r is the annual interest rate.
# n is the number of times per year the interest is compounded.
# t is the specified number of years.

# Inputs
principal = float(input('Enter the principal amount that was originally deposited into the account: '))
interest_rate = float(input('Enter the annual interest rate: '))
years = int(input('Enter the number of years the principal is allowed to grow: '))
n = int(input('Enter the number of times the interest is compounded: '))

# Process
future_value = principal * (1 + (interest_rate / n)) ** (n * years)

# Output
print(f"Amount accrued: ${future_value:,.2f}")