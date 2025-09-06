# Adding a new user if the current user is not in the file dump.
from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username, if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        correct_username = input(f"Is this the correct username: {username}? [y/n] ")
        if correct_username.lower() == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

def get_new_username(path):
    """Prompt for a new username."""
    username = input('What is your name? ')
    contents = json.dumps(username.lower())
    path.write_text(contents)
    return username

greet_user()