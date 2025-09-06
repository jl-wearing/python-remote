# Program to determine which of 2 rectangles has a greater area.

# Input
length1 = float(input('Enter the length of the first rectangle: '))
width1 = float(input('Enter the width of the first rectangle: '))
length2 = float(input('\nEnter the length of the second rectangle: '))
width2 = float(input('Enter the width of the second rectangle: '))

# Process
larger_area = (length1 * width1) if (area1 := length1 * width1) > \
                                    (area2 := length2 * width2) else (length2 * width2)

# Output
print(f"The larger area of {area1:.2f} and {area2:.2f} is {larger_area:.2f}")