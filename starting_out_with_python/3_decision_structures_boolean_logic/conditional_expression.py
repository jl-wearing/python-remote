# Program to showcase the conditional operator.

# Input
num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

# Process
maximum = num1 if num1 > num2 else num2

# Output
print(f"The larger of {num1} and {num2} is {maximum}.")