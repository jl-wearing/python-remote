# The walrus operator assigns a value to a variable, and returns that value.

print(result := 27)

print(age := int(input('Enter your age: ')))

# Mainly used in boolean expressions.
# Input
hours_worked = int(input('Enter your hours worked: '))
hourly_wage = float(input('Enter your hourly wage: '))

if (pay := hours_worked * hourly_wage) > 40:
    print('You worked overtime.')