# Program to calculate the factorial of a number.

def factorial(x: int) -> int | None:
    """Return the factorial of a number."""
    if x <= 0:
        return
    if x == 1:
        return 1

    return x * factorial(x - 1)


def main():
    """Main function for testing the factorial function."""
    print(factorial(5), factorial(4), factorial(3), factorial(2), factorial(1), factorial(0), sep='\n')


# Call the main function.
if __name__ == '__main__':
    main()