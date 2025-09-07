# Program to display a table of celsius to fahrenheit conversions.

def main():
    """Main function."""
    print("Program to display a table of celsius to fahrenheit conversions from 0 to 20.")
    print("Celsius\t\t\tFahrenheit")
    print("="*30)
    for i in range(21):
        print(f"{i}{(9/5) * i + 32:>22.2f}")


# Call the main function.
if __name__ == '__main__':
    main()