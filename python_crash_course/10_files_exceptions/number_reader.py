# Program to read JSON data from a file.
import json
from pathlib import Path

def main():
    """main function."""
    # Get the file to read data from.
    path = Path('numbers.json')

    # Get the contents of the file.
    contents = path.read_text()

    # Convert the JSON to Python data structure.
    numbers = json.loads(contents)

    # Display the data.
    print(numbers)

# Call the main function.
if __name__ == '__main__':
    main()