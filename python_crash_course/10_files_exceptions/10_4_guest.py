# Program to write the name of a guest to a file.
from pathlib import Path

# Constants used by the program.
file_name = 'guest.txt'

def get_input() -> str:
    """Get the name of a guest from the terminal."""
    name = input('Enter your name: ')
    return name.lower()

def write_to_file(name: str) -> None:
    """Write the guest name to a file."""
    path = Path(file_name)

    # Write the name to the file.
    path.write_text(name)

def main():
    """Mainline logic for writing a guest to a file."""
    # Get the name of the guest.
    name = get_input()

    # Write the name to the file.
    write_to_file(name)

# Call the main function.
if __name__ == '__main__':
    main()