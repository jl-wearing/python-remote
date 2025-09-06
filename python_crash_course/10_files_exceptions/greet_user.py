# Program to greet a user stored in the JSON file.
from pathlib import Path
import json

def main():
    """Mainline logic for remembering a user stored in a file."""
    path = Path('username.json')
    contents = path.read_text()
    username = json.loads(contents)

    print(f"Welcome back, {username.title()}!")

# Call the main function.
if __name__ == '__main__':
    main()