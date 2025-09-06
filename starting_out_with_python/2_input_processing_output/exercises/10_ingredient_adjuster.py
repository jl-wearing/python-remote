# Program to adjust the measurements to make a certain amount of cookies.

# Constants used by the program.
COOKIES = 48    # The recipe makes 48 cookies.
CUPS_OF_SUGAR = 1.5
CUPS_OF_BUTTER = 1
CUPS_OF_FLOUR = 2.75

# Input the number of cookies the user wants to make.
number_of_cookies_to_make = int(input('How many cookies do you want to make?: '))

# Calculate the new measurements.
new_sugar_cups = (CUPS_OF_SUGAR * number_of_cookies_to_make) / COOKIES
new_butter_cups = (CUPS_OF_BUTTER * number_of_cookies_to_make) / COOKIES
new_flour_cups = (CUPS_OF_FLOUR * number_of_cookies_to_make) / COOKIES

# Output the new measurements.
print(f"Cups of sugar required: {new_sugar_cups}")
print(f"Cups of butter required: {new_butter_cups}")
print(f"Cups of flour required: {new_flour_cups}")