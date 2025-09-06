# Program to convert seconds to hours, minutes, and remaining seconds.

# input the number of seconds to convert.
seconds = int(input('Enter the number of seconds: '))

# process
# calculate the number of hours
hours = seconds // 3600

# calculate the number of minutes
minutes = (seconds % 3600) // 60

# calculate the remaining number of seconds.
remaining_seconds = seconds % 3600 % 60

# output
print('Here is the time in hours, minutes, and seconds:')
print('Hours', hours)
print('Minutes', minutes)
print('Seconds', remaining_seconds)