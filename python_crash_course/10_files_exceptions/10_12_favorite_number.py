# Program to store and retrieve a person's favorite number.
from pathlib import Path
import json

def get_favorite_number(path):
    """Get a user's favorite number."""
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        return favorite_number
    else:
        return None


def store_favorite_number(path):
    """Store a user's favorite number."""
    favorite_number  = input('What is your favorite number? ')
    contents = json.dumps(favorite_number)
    path.write_text(contents)

    print(f"We will store your favorite number when you come back!")


def main():
    """Main function to either retrieve a user's favorite number or store it for later."""
    path = Path('favorite_number.json')
    favorite_number = get_favorite_number(path)
    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}!")
    else:
        store_favorite_number(path)

# Call the main function
if __name__ == '__main__':
    main()