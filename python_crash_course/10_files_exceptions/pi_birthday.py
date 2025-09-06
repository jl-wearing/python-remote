# Program to determine if my birthday is in the first million digits of pi.
from pathlib import Path

def main():
    """Main function."""
    path = Path(r'pi_million_digits.txt')

    if path.exists():
        # Retrieve the contents of the file.
        contents = path.read_text()

        # Return a list of every line in contents.
        lines=contents.splitlines()

        # Obtain a single string of every line.
        pi_digits = ''
        for line in lines:
            pi_digits += line.strip()

        # Input birthday.
        birthday = input('Enter your birthday in mmddyy: ')

        # Check if birthday is in first million digits of pi.
        if birthday in pi_digits:
            print("Your birthday is in the first million digits of pi.")
        else:
            print("Your birthday is not in the first million digits of pi.")
    else:
        print('File not found')

# Call the main function.
if __name__ == '__main__':
    main()