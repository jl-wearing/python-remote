# Program to store a user's name for later reference.
from pathlib import Path
import json

def main():
    """Program to store a user's name for later reference."""
    name = input('What is your name? ')

    path = Path('username.json')
    contents = json.dumps(name.lower())
    path.write_text(contents)

    print(f"We'll remember you when you come back, {name.title()}!")

# Call the main function.
if __name__ == '__main__':
    main()