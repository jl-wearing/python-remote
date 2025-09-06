# Program to add 2 numbers.
from pathlib import Path

def get_input() -> tuple[int, int]:
    """Read two numbers from the user."""
    while True:
        try:
            # Get the first number.
            first_number = int(input('Enter the first number: '))

            # Get the second number.
            second_number = int(input('Enter the second number: '))

            return first_number, second_number
        except ValueError:
            print(f"You didn't enter a number. Try again.")

def add(a: int, b: int) -> int:
    """Function to add two numbers."""
    return a + b

def main():
    """Main function for adding 2 numbers."""
    print('Enter 2 numbers and I will add them.')

    # Input
    first_number, second_number = get_input()

    # Process
    total = add(first_number, second_number)

    # Output
    print(f"{first_number} + {second_number} = {total}")

# Call the main function.
if __name__ == '__main__':
    main()