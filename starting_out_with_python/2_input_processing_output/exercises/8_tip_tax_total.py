# Program to generate a receipt of a restaurant.

# Constants used by the program.
TIP_PERCENTAGE = 0.18
SALES_TAX_PERCENTAGE = 0.07

# Input the meal price.
meal_price = float(input('Enter the meal price: '))

# Calculate the tip.
tip = meal_price * TIP_PERCENTAGE

# Calculate the sales tax.
tax = meal_price * SALES_TAX_PERCENTAGE

# Calculate the total price.
total = meal_price + tip + tax

# Display each price.
print(f"Meal Price: ${meal_price:,.2f}")
print(f"Sales Tax: ${tax:,.2f}")
print(f"Tip Amount: ${tip:,.2f}")
print(f"Total: ${total:,.2f}")