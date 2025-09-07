# Program to add the sum of positive numbers.

def input_positive_numbers() -> list[int]:
    """Input positive numbers."""
    data = []
    while True:
        # Input
        number = int(input("Enter a positive number to total, or insert any negative number to quit: "))
        if number < 0:
            break
        data.append(number)

    return data


def summate(data: list[int]) -> int:
    """Sum the numbers in the list of positive numbers."""
    return sum(data)


def main():
    """Main function."""
    # Input data.
    data = input_positive_numbers()

    # Sum the numbers.
    total = summate(data)

    # Output
    print(f"\nThe sum of numbers is: {total}.")


# Call the main function.
if __name__ == '__main__':
    main()