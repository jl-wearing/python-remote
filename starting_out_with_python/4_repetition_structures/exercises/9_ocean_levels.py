# Program to determine how much ocean levels rise after x number of years.

def get_number_of_years_ocean_rises() -> int:
    """Get the number of years the ocean levels rise."""
    years = int(input('Enter the number of years: '))

    # Input validation.
    while years < 0:
        print('You must enter a positive year.')
        years = int(input('Enter the number of years: '))

    return years


def get_level_rise() -> float:
    """Get the measured ocean level rise per year in mm."""
    return float(input('Enter the measured ocean level rise in mm per year: '))


def main():
    """Main function."""
    # Get the number of years ocean levels rises.
    years = get_number_of_years_ocean_rises()

    # Get the measured rise per year in mm.
    measured_rise = get_level_rise()

    # Output
    total_rise = 0
    print("\nYear\t\t\tMeasured Ocean Level Rise")
    print("="*50)
    for i in range(0, years + 1):
        print(f"Year {i}: {total_rise:^30.2f}")
        total_rise += measured_rise


# Call the main function.
if __name__ == '__main__':
    main()