# Program to draw a triangle on the screen.

def get_input() -> int:
    """Get the length of the triangle from the user."""
    length = int(input('Enter the length of the triangle: '))

    # Validate the input
    while length < 0:
        print('Error: The length must be greater than 0.')
        length = int(input('Enter the length of the triangle: '))

    return length


def draw_triangle(length: int) -> None:
    """Draw a triangle on the screen."""
    for i in range(length):
        for j in range(i+1):
            print('*', end='')
        print()


def main():
    """Main function for drawing triangles on the screen."""
    # Get the length of the triangle to draw.
    length = get_input()

    # Draw the rectangle on the screen.
    draw_triangle(length)


# Call the main function.
if __name__ == '__main__':
    main()