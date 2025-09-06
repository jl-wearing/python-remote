# Program to display a day of the week based on a user's input.

# Constants used by the program.
MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7

# Input
day_of_the_week = int(input('Enter a number 1 through 7 to display a day of the week: '))

# Process
message = ''
if day_of_the_week == MONDAY:
    message = "The day is Monday."
if day_of_the_week == TUESDAY:
    message = "The day is Tuesday."
if day_of_the_week == WEDNESDAY:
    message = "The day is Wednesday."
if day_of_the_week == THURSDAY:
    message = "THe day is Thursday."
if day_of_the_week == FRIDAY:
    message = "The day is Friday."
if day_of_the_week == SATURDAY:
    message = "The day is Saturday."
if day_of_the_week == SUNDAY:
    message = "The day is Sunday."
if day_of_the_week < 1 or day_of_the_week > 7:
    message = "Invalid number entered."

# Output
print(message)