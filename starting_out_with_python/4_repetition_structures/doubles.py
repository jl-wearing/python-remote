# Program to add numbers.

def main():
    """Main function for adding numbers."""
    number = 1
    while number <= 10:
        print(f"{number} + {number} = {number + number}")
        number += 1

# Call the main function.
if __name__ == "__main__":
    main()