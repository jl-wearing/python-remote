# Program to calculate miles per gallon.
#mpg = miles driven / gallon of gas used.

# Input the miles driven.
miles_driven = float(input('Enter the number of miles driven: '))

# Input the gallon of gas used.
gallon_used = float(input('Enter the total gallon use: '))

# Calculate the miles per gallon.
miles_per_gallon = f"{miles_driven/gallon_used:,.2f}"

# Output the miles per gallon.
print(f"Miles per gallon: {miles_per_gallon} mpg")