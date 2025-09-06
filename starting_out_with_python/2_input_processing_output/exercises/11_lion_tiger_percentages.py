# Program to calculate the percentage of lions and tigers in a zoo as a percentage.

# Input the number of lions in the zoo.
lions = int(input('Enter the number of lions in the zoo: '))

# Input the number of tigers in the zoo.
tigers = int(input('Enter the number of tigers in the zoo: '))

# Calculate the total number of cats.
cats = lions + tigers

# Display the percentages of each cat.
print(f'Percentage of tiger population: {100 * (lions/cats):.2f}%')
print(f'Percentage of lion population: {100 * (tigers/cats):.2f}%')