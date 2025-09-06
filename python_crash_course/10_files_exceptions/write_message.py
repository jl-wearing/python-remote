# Program to write data to a file.
from pathlib import Path

def main():
    """Main function to write data to a file."""
    # Set a path to the file.
    path = Path('programming.txt')

    # Write data to the file
    contents = 'I love programming.\n'
    contents += 'I love creating new games.\n'
    contents += 'I also love working with data.\n'
    path.write_text(contents)

# Call the main function.
if __name__ == '__main__':
    main()