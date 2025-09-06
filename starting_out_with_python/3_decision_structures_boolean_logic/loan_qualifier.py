# Program to determine whether an employee qualifies for a loan.

# Constants used by the program.
MIN_SALARY = 30_000.00
MIN_YEARS = 2

# Input
annual_salary = float(input('Enter your annual salary: '))
years_on_job = int(input('Enter the number of years you have worked for this corporation: '))

# Process and output
if annual_salary > MIN_SALARY and years_on_job > MIN_YEARS:
    print('You qualify for the loan.')
else:
    if annual_salary < MIN_SALARY:
        print(f"Sorry, you need to make at least ${MIN_SALARY} to qualify the loan.")

    if years_on_job < MIN_YEARS:
        print(f"Sorry, you need to work for at least {MIN_YEARS} to qualify for a loan.")