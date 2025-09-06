# Program to display a table of speeds in KMH.

def main():
    """Mainline logic for displaying a table of speed values in KMH."""
    # Constants used by the program.
    MILES_PER_KM = 0.6214

    # Output
    print('KPH\t\tMPH')
    print('-'*20)
    for speed in range(60, 131, 10):
        miles = speed * MILES_PER_KM
        print(f"{speed}\t\t{miles:.2f}")


# Call the main function
if __name__ == '__main__':
    main()