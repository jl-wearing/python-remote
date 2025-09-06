# Program to calculate the number of bugs collected for 5 days.

def get_number_of_bugs_collected() -> int:
    """Get the number of bugs collected."""
    number_of_bugs = int(input('How many bugs have you collected?: '))

    # Input validation.
    while number_of_bugs < 0:
        print('You cannot collect negative bugs, enter a number > 0: ')
        number_of_bugs = int(input())

    return number_of_bugs


def main():
    """Main function used to collect bugs for a number of days."""
    # Constants used by the program.
    NUMBER_OF_DAYS = 5

    # Determine the total number of bugs collected.
    total = 0
    for i in range(1, NUMBER_OF_DAYS + 1):
        print(f'For day {i}: ')
        number_of_bugs = get_number_of_bugs_collected()
        print()
        total += number_of_bugs

    # Output
    print(f"\nTotal number of bugs collected over {NUMBER_OF_DAYS} days: {total}")


# Call the main function.
if __name__ == '__main__':
    main()