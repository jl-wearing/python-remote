# Program to generate a receipt after purchasing items from a store.
SALES_TAX = 0.07

# Input each item's price.
prices = []
for i in range(1, 6):   # purchasing 5 items.
    prices.append(float(input(f'Enter the price of item #{i}: ')))

# Calculate the subtotal price.
subtotal = sum(prices)

# Calculate the sales tax.
tax = subtotal * SALES_TAX

# Calculate the total.
total = subtotal + tax

# Output the receipt.
print(f'Subtotal: ${subtotal:,.2f}')
print(f'Tax: ${tax:,.2f}')
print(f'Total: ${total:,.2f}')