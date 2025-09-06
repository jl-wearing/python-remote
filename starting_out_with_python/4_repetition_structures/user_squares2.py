# Program to display a table of squares from [start, end].

def get_input() -> tuple[int, int]:
    """Get the starting and ending values."""
    print('This program displays a list of square numbers from starting value to ending value.')
    start = int(input('Enter the starting value: '))
    end = int(input('Enter the ending value: '))

    return start, end

def display_table(start: int, end: int) -> None:
    """Display the table of square numbers from starting value to ending value."""
    if start > end:
        raise ValueError('Start value cannot be greater than end value.')

    print('Number\tSquare')
    print('='*20)
    for i in range(start, end+1):
        print(f'{i}\t\t{i*i}')

def main():
    """Main function for displaying square numbers from starting value to ending value."""
    # Get the starting and ending values.
    start, end = get_input()

    # Display the table.
    display_table(start, end)


# Call the main function.
if __name__ == '__main__':
    main()