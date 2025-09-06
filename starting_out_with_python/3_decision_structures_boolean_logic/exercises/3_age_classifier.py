# Program to determine if a user is an infant, child, teenager or adult.

# Constants used by the program.
INFANT = 1
CHILD = 13
TEENAGER = 20

# Input
age = int(input('Enter your age: '))

# Process
if age <= INFANT:
    message = "You are an infant."
elif INFANT < age < CHILD:
    message = "You are a child."
elif CHILD <= age < TEENAGER:
    message = "You are a teenager."
else:
    message = "You are an adult."

# Output
print(message)