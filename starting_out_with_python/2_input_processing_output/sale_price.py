# Program to calculate the price of an item after applying a discount.
DISCOUNT_PERCENTAGE = 0.2

# Get the original price of an item.
original_price = float(input("Enter the item's original price: "))

# Calculate the amount for the discount.
discount = original_price * DISCOUNT_PERCENTAGE

# Calculate the sale price.
sale_price = original_price - discount

# Display the sale price.
print('Your sale price is $', sale_price)