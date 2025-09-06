# Program to determine the secondary color obtained from mixing primary colors.

# Constants used by the program.
RED = 'red'
BLUE = 'blue'
YELLOW = 'yellow'
PURPLE = 'purple'
ORANGE = 'orange'
GREEN = 'green'

# Input
color1 = input('Enter a primary color: (red/blue/yellow): ')
color2 = input('Enter another primary color different from the first selection: (red/blue/yellow): ')

# Process
secondary_color = ''
if color1 == color2:
    print('Error! try again!')
else:
    if color1 == RED:
        if color2 == BLUE:
            secondary_color = PURPLE
        if color2 == YELLOW:
            secondary_color = ORANGE
    elif color1 == BLUE:
        if color2 == RED:
            secondary_color = PURPLE
        if color2 == YELLOW:
            secondary_color = GREEN
    elif color1 == YELLOW:
        if color2 == RED:
            secondary_color = ORANGE
        if color2 == BLUE:
            secondary_color = GREEN
    else:
        print('Error! try again!')

# Output
if secondary_color:
    print(f"\nThe result of mixing {color1} and {color2} is {secondary_color}.")