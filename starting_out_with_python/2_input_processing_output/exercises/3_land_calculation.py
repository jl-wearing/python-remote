# Program to convert square feet to acres.
ONE_ACRE = 43_560 # one acre = 43560 square feet

# Input the square feet
print('This program converts square feet to acres.')
square_feet = float(input('Enter the square feet you want converted: '))

# Calculate acres as square_feet / one_acre
acres = square_feet / ONE_ACRE

# Output the acres
print(f"{square_feet:,.2f} square feet in acres: {acres:,.2f} acres.")