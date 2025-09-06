# Program to write a list of guests to a guest book file.
from pathlib import Path

# Constants used by the program.
file_name = 'guest_book.txt'

def get_names() -> str:
    """Get the names of guests from the keyboard."""
    names = ''
    while True:
        # Retrieve a name from the user.
        name = input('Enter a guest-name or Q/q to quit: ')
        if name == 'Q' or name == 'q':
            break
        names += name + '\n'

    return names

def write_names_to_file(names: str):
    """Write guest names to a file."""
    path = Path(file_name)

    # Write the names to the file.
    if names:
        path.write_text(names)

def main():
    """Main function to write a list of guests to a file."""
    # Get the guest names.
    names = get_names()

    # Write the names to the file.
    write_names_to_file(names)

# Call the main function.
if __name__ == '__main__':
    main()