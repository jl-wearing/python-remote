# Program to calculate the average rainfall for a number of years.
from unittest import case


def get_number_of_years() -> int:
    """Get the number of years to collect data for."""
    years = int(input('Enter the number of years of rainfall figures: '))

    # Input validation.
    while years < 0:
        print('Please enter a positive integer')
        years = int(input('Enter the number of years of rainfall figures: '))

    return years


def get_rainfall():
    """Get rainfall data."""
    measured_rainfall = float(input('Enter the measured rainfall value: '))

    # Input validation.
    while measured_rainfall < 0:
        measured_rainfall = float(input('Enter the measured rainfall value: '))

    return measured_rainfall


def get_month(i: int) -> str:
    """Get the month."""
    match i:
        case 1:
            return 'January'
        case 2:
            return 'February'
        case 3:
            return 'March'
        case 4:
            return 'April'
        case 5:
            return 'May'
        case 6:
            return 'June'
        case 7:
            return 'July'
        case 8:
            return 'August'
        case 9:
            return 'September'
        case 10:
            return 'October'
        case 11:
            return 'November'
        case 12:
            return 'December'
        case _:
            return "Invalid month"


def main():
    """Main function."""
    # Constants used by the program.
    NUMBER_OF_MONTHS = 12

    # Input number of years to collect data for.
    years = get_number_of_years()

    # Collect rainfall data.
    total_rainfall = 0.0
    for i in range(1, years+1):
        for j in range(1, NUMBER_OF_MONTHS+1):
            print(f"Enter data for month {get_month(j)}: ")
            total_rainfall += get_rainfall()


    # Output
    print(f"\nTotal rainfall: {total_rainfall:.2f}mm")


# Call the main function.
if __name__ == '__main__':
    main()