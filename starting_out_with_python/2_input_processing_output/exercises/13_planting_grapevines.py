# Program to calculate the number of grapevines that will fit in a row.
# v = (r - 2e) / s

# Input
r = float(input('Enter the length of each row: '))
e = float(input('Enter the amount of space used by an end-post assembly: '))
s= float(input('Enter the amount of space between vines: '))

# Process
v = (r - 2 * e) / s

# Output
print(f"Number of grapevines that will fit in a row: {int(v):,d}")