# Program to let a user generate a table of squares.

def get_input() -> int:
    """Get the largest square the user wants."""
    print('This program displays a list of numbers & their squares.')
    return int(input('How high should I go?: '))

def display_table(end: int) -> None:
    """Display the table of squares."""
    if end < 0:
        return

    print('Number\tSquare')
    print('='*20)
    for i in range(1, end+1):
        print(f'{i}\t\t{i*i}')


def main():
    """Main function for displaying the table of squares."""
    # Get the end value.
    end = get_input()

    # Display the table
    display_table(end)


# Call the main function.
if __name__ == '__main__':
    main()