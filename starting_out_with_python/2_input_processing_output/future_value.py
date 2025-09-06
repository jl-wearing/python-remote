# Program to calculate the present value required to obtain a future value after a certain number of years.

# Input the future value required
future_value = float(input('Enter the future value of the account: '))

# Input the number of years the account will grow
years = int(input('Enter the number of years the account will grow: '))

# Input the annual interest rate
annual_interest_rate = float(input('Enter the annual interest rate: '))

# Process
# Calculate the present value required
present_value = future_value / ((1.0 + annual_interest_rate) ** years)

# Output the present value required
print(f"Amount required to grow your account to ${future_value:.2f}"
      f" after {years} years: ${present_value:.2f}")