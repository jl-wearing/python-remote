# Program to congratulate a student if their average score is high enough.

# Constants used by the program.
HIGH_SCORE = 95

# Input
test1= float(input('Enter the test 1 score: '))
test2 = float(input('Enter the test 2 score: '))
test3 = float(input('Enter the test 3 score: '))

# Process
average = (test1 + test2 + test3) / 3.0

# Output
print(f"The average score is: {average:.2f}")
if average >= HIGH_SCORE:
    print("Congratulations! This is a high average!")