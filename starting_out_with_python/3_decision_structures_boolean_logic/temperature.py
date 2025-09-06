# This program assists a technician in the process of checking a substance's temperature.

# Constants used by the program.
MAX_TEMP = 102.5

def main():
    """Main function for checking temperature readings."""
    # Get the substance's temperature
    current_temperature = float(input("Enter the substance's temperature: "))

    while current_temperature > MAX_TEMP:
        print("The temperature is too high.")
        print("Turn down the thermostat and wait 5 minutes.")
        print("Then take the temperature reading again.")

        current_temperature = float(input("Enter the substance's temperature: "))

    # Output
    print("The temperature is acceptable.")
    print("Check again in 15 minutes.")

# Call the main function.
if __name__ == '__main__':
    main()