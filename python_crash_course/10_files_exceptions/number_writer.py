# Program to write data to a file in JSON format.
import json
from pathlib import Path

def main():
    """main function."""
    # Create a list of numbers to store.
    numbers = [1, 2, 3, 4, 5]

    # Create a file to write to.
    path = Path('numbers.json')

    # Convert the data structure to JSON format.
    contents = json.dumps(numbers)

    # Write the data to the file.
    path.write_text(contents)

# Call the main function.
if __name__ == '__main__':
    main()