# Program to store a username if it is their first time, or greet the user if
# are returning.
from pathlib import Path
import json

def main():
    """Main function."""
    path = Path('username.json')

    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username.title()}!")
    else:
        username = input('What is your name? ')
        contents = json.dumps(username.lower())
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username.title()}!")

# Call the main function.
if __name__ == '__main__':
    main()