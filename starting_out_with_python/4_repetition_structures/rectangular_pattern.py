# Program to display a rectangle on the console.

def get_input() -> tuple[int, int]:
    """Get the length and width of a rectangle from the user."""
    width = int(input('Enter the width of the rectangle: '))
    height = int(input('Enter the height of the rectangle: '))

    # Validate the width and height inputs
    while width < 0:
        print('Error: The width must be greater than 0.')
        width = int(input('Enter the width of the rectangle: '))

    while height < 0:
        print('Error: The height must be greater than 0.')
        height = int(input('Enter the height of the rectangle: '))

    return width, height


def draw_rectangle(width: int, height: int) -> None:
    """Draw a rectangle on the screen."""
    for i in range(width):
        for j in range(height):
            print('*', end='')
        print()


def main():
    """Mainline logic for drawing rectangles on the screen."""
    # Get the width and height of the rectangle.
    width, height = get_input()

    # Draw the rectangle.
    draw_rectangle(width, height)


# Call the main function.
if __name__ == '__main__':
    main()