# Program to display the contents of a file.
from pathlib import Path

def read_file(filename: str) -> str or None:
    """Function to read the contents of a file."""
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return None
    else:
        return contents

def display_file_content(contents: str) -> None:
    """Function to display the contents of a file."""
    for line in contents.splitlines():
        print(line)
    print()

def main():
    """Mainline logic for displaying the contents of a file."""
    files = ['cats.txt', 'dogs.txt']

    for file in files:
        # Attempt to read the file.
        contents = read_file(file)

        # Display the content in the file.
        if contents:
            display_file_content(contents)

# Call the main function.
if __name__ == '__main__':
    main()