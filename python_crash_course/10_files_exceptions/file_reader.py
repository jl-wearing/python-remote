# Program to read from a file.
import sys
from pathlib import Path

def main():
    """Main function to read from a file."""
    # Retrieve a pointer to the file.
    path = Path(r'pi_digits.txt')
    if path.exists():
        # Retrieve the contents of the file.
        contents = path.read_text()

        # Strip any whitespace.
        contents = contents.rstrip()

        # Display the contents.
        print(contents)
    else:
        print('File not found')


# Call the main function.
if __name__ == '__main__':
    main()