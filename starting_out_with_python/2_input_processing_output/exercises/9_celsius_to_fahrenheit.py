# Program to convert celsius to fahrenheit.
# f = (9/5)C + 32

# Input the celsius amount
celsius= float(input('Enter the temperature in celsius: '))

# Convert the celsius to fahrenheit.
fahrenheit = (9/5) * celsius + 32

# Output the fahrenheit amount.
print(f"{celsius:,.2f} degrees celsius to fahrenheit: {fahrenheit:,.2f} degrees fahrenheit")