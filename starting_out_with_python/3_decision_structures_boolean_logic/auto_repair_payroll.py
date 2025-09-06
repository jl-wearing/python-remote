# Program to calculate the pay of an employee at a repair shop.

# Constants used by the program.
OT_MULTIPLIER = 1.5
BASE_HOURS = 40

# Input
hours_worked = float(input('Enter the number of hours worked in the week: '))
hourly_wage = float(input('Enter your hourly wage: '))

# Process
# Calculate the base pay
base_pay = hourly_wage * BASE_HOURS
overtime_pay = 0.0

# Calculate overtime pay
if hours_worked > BASE_HOURS:
    # Calculate the number of hours worked over the base hours.
    overtime_hours = hours_worked - BASE_HOURS

    # Calculate the overtime pay.
    overtime_pay = overtime_hours * OT_MULTIPLIER * hourly_wage

# Calculate the total pay.
total_pay = overtime_pay + base_pay

# Output
print(f"The gross pay is: ${total_pay:,.2f}.")