# Program to display property taxes.

def main():
    """Main function for displaying property taxes."""
    # Constants used by the program.
    TAX_FACTOR = 0.0065

    # Input
    lot_number = int(input('Enter the lot number: '))

    # Process
    while lot_number != 0:
        property_value = float(input('Enter the property value: '))
        property_tax = property_value * TAX_FACTOR

        # Output
        print(f"Property Tax: ${property_tax:.2f}\n")

        # Input
        lot_number = int(input('Enter a new lot number, or 0 to terminate: '))


# Call the main function.
if __name__ == '__main__':
    main()