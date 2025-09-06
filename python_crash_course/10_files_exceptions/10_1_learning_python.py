# Program to read from a file.
from pathlib import Path

def main():
    """Main function."""
    # Copy the file to main memory.
    path = Path(r'learning_python.txt')

    if path.is_file():
        # Read the contents of the file.
        contents = path.read_text()

        # Print the content by reading the entire file.
        print(contents, '\n')

        # Print the contents by storing the lines in a list.
        for line in contents.splitlines():
            print(line)
        print()

# Call the main function.
if __name__ == '__main__':
    main()