# Program to implement try-except blocks.

def main():
    """Main function."""
    try:
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter another number: '))

        result = num1 / num2
        print(f"result: {result:.2f}")
    except ZeroDivisionError:
        print("You can't divide by zero.")
    except ValueError:
        print("You didn't enter a number.")
    except Exception as err:
        print(err)

# Call the main function.
if __name__ == '__main__':
    main()