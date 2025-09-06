# Program to read from a file 2.
from pathlib import Path

def main():
    """Main function to read from a file 2."""
    path = Path(r'pi_digits.txt')
    if path.exists():
        # Retrieve the contents from the file.
        contents = path.read_text()

        # Retrieve the contents as a list.
        lines = contents.splitlines()

        # Output each line.
        for line in lines:
            print(line.strip(), end='')
    else:
        print('File not found')

# Call the main function.
if __name__ == '__main__':
    main()