# Program to assist a technician with checking the temperature of a substance.

def main():
    """Mainline logic for checking and adjusting a substance's temperature."""
    # Constants used by the program.
    THRESHOLD = 102.5

    # Get the temperature of the substance.
    temperature= float(input('Enter the substance\'s temperature: '))

    while temperature > THRESHOLD:
        # Tell the technician to lower the temperature.
        print('Lower the thermostat and wait 5 minutes.')
        print('Then take the temperature reading again.')

        # Get the new temperature reading.
        temperature = float(input('What is the new temperature?: '))

    # The temperature is now ok.
    print('\nThe temperature is acceptable and you can check again in 15 minutes.')

# Call the main function.
if __name__ == '__main__':
    main()