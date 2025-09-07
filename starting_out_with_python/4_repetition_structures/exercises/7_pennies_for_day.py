# Program to calculate how many pennies a user would earn if they double every day.

def get_number_of_days() -> int:
    """Get the number of days pennies will double for."""
    days = int(input('Enter the number of days you are collecting pennies for: '))

    # Input validation.
    while days < 0:
        print("Please enter a positive number.")
        days = int(input('Enter the number of days you are collecting pennies for: '))

    return days


def display_table(number_of_days: int) -> None:
    """Display a table of days pennies will double for."""
    print("Day\t\t\tPenny Size")
    print("="*30)
    for i in range(1, number_of_days + 1):
        print(f"{i}{i*i:>20}")

def main():
    """Main function."""
    # Input
    number_of_days = get_number_of_days()

    # Output
    display_table(number_of_days)


# Call the main function.
if __name__ == '__main__':
    main()