# Program to display the first 50 decimal places of pi read from a file.
from pathlib import Path

def main():
    """Main function to read and display the first 50 digits of pi from a file."""
    path = Path(r'pi_million_digits.txt')

    if path.exists():
        # Retrieve the contents of the file.
        contents = path.read_text()

        # Return the contents as a list of lines.
        lines = contents.splitlines()

        # Form a single string of all lines.
        pi_digits = ''
        for line in lines:
            pi_digits += line.strip()

        # Output the first 50 decimal places of pi.
        print(pi_digits[:52])
    else:
        print('file not found')

# Call the main function
if __name__ == '__main__':
    main()