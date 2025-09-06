# Program to determine the grade of a student.

# Input
grade = float(input('Enter your test score: '))

# Process
if grade >= 90:
    score = 'A'
elif grade >= 80:
    score = 'B'
elif grade >= 70:
    score = 'C'
elif grade >= 60:
    score = 'D'
else:
    score = 'F'


# Output
print(f'Your grade is {score}.')