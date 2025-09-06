# Program to convert seconds to hours, minutes, and remaining seconds.

# input
seconds = int(input('Enter the number of seconds to convert: '))

# process
# calculate the number of hours in those seconds
hours = seconds // 3600

# calculate the remaining number of minutes from the hours
remaining_minutes = seconds % 3600
minutes = remaining_minutes // 60

# calculate the remaining number of seconds from the minutes.
remaining_seconds = remaining_minutes % 60

# output the hours, minutes and seconds
print(f"HH:MM:SS: {hours:02d}:{minutes:02d}:{remaining_seconds:02d}\n")