# Program to determine if an object's weight is too high or too low.

# Constants used by the program.
GRAVITATIONAL_CONSTANT= 9.8
HEAVY_WEIGHT = 500
LIGHT_WEIGHT = 100

# Input
mass = float(input('Enter the mass of the object: '))

# Process
weight = mass * GRAVITATIONAL_CONSTANT
if weight < LIGHT_WEIGHT:
    message = "This object is too light."
elif weight > HEAVY_WEIGHT:
    message = "This object is too heavy."
else:
    message = "This object has a normal weight."

# Output
print(message)