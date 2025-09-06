# Program to compute different taxes of an item purchased.

STATE_TAX_PERCENTAGE = 0.05
COUNTRY_TAX_PERCENTAGE = 0.025

# Input the purchase price
price = float(input('Enter the purchase price: '))

# Calculate the state tax.
state_tax = price* STATE_TAX_PERCENTAGE

# Calculate the country tax.
country_tax = price * COUNTRY_TAX_PERCENTAGE

# Calculate the total tax amount.
total_tax = country_tax + state_tax

# Calculate the total sale price.
total = total_tax + price

# Output the receipt.
print(f"Purchase amount: ${price:,.2f}")
print(f"Sales Tax: ${state_tax:,.2f}")
print(f"Country Tax: ${country_tax:,.2f}")
print(f"Total Tax: ${total_tax:,.2f}")
print(f"Total: ${total:,.2f}")