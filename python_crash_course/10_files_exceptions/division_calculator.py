# Program to divide 2 numbers.

def main():
    """Mainline logic for dividing 2 numbers."""
    print('Give me 2 numbers and I\'ll divide them.')
    print("Enter 'q' to quit.")
    while True:
        first_number = input('\nFirst number: ')
        if first_number == 'q':
            break

        second_number = input('Second number: ')
        if second_number == 'q':
            break

        try:
            answer = int(first_number) / int(second_number)
        except ZeroDivisionError:
            print("You can't divide by zero.")
        except ValueError:
            print("You didn't enter a number.")
        except Exception as err:
            print("Something went wrong.", str(err))
        else:
            print(f"{answer:.2f}")

# Call the main function.
if __name__ == '__main__':
    main()