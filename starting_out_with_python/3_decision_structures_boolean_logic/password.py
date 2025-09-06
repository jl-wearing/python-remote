# Program to compare 2 strings.

# Constants used by the program.
CORRECT_PASSWORD = 'prospero'

# Input
password = input('Enter the password: ')

# Process and Output
if password == CORRECT_PASSWORD:
    print('Password Accepted!')
else:
    print('Sorry, that is the wrong password.')