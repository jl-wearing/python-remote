# Program to read from a file.
from pathlib import Path

def main():
    """Main function to read from a file."""
    path = Path(r'pi_digits.txt')

    if path.exists():
        # Read the contents of the file.
        contents = path.read_text()

        # Store each line in a list.
        lines = contents.splitlines()

        # form a single string of every line.
        pi = ''
        for line in lines:
            pi += line.lstrip()

        # Output the final string.
        print(pi)
        print(len(pi))
    else:
        print('File not found')

# Call the main function.
if __name__ == '__main__':
    main()