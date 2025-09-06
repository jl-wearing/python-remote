# Program to accumulate numbers.

def main():
    """Main function for summing numbers."""

    # Constants used by the program.
    MAX_VALUE = 5   # summing up 5 times.

    accumulator = 0
    for i in range(1, MAX_VALUE+1):
        # Get the number to read.
        number = int(input('Enter the number to add to the accumulator: '))
        accumulator += number

    # Display the total.
    print(f"Total: {accumulator}")


# Call the main function.
if __name__ == '__main__':
    main()