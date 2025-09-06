# Program to replace all occurrences of a word with another word.
from pathlib import Path

def main():
    """Main function to test how the replace() method works."""
    # Copy the file to main memory.
    path = Path(r'learning_python.txt')

    if path.exists():
        # Retrieve the contents of the file.
        contents = path.read_text()

        # Replace every occurrence of 'Python' with 'C'
        contents = contents.replace('Python', 'C')

        # Output
        print(contents)

# Call the main function.
if __name__ == '__main__':
    main()