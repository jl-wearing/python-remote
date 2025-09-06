# Program to determine if the day * month equals the year.

# Input
day = int(input('Enter a day of the month: '))
month = int(input('Enter a month of the year: '))
year = int(input('Enter the last 2 digits of any year, .e.g 70, for 1970 etc: '))

# Process
sentinel = True if (date := month * day) == year else False

# Output
if sentinel:
    print(f'{day}/{month}/{year}')
else:
    print(f'{date} is not equal to {year}')