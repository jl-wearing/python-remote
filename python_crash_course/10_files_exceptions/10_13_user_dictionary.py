from pathlib import Path
import json

def get_user_data(path):
    """Get the user's information."""
    if path.exists():
        contents = path.read_text()
        user_information = json.loads(contents)
        return user_information
    else:
        return None

def store_user_data(path):
    """Store the user's information."""
    user_information = {}

    name = input("What is your name? ")
    user_information['name'] = name

    while True:
        try:
            age = int(input("How old are you? "))
            user_information['age'] = age
            break
        except ValueError:
            print("Please enter a number.")

    occupation = input("What is your occupation? ")
    user_information['occupation'] = occupation.lower()

    contents = path.write_text(json.dumps(user_information))

    print("Your information has been stored!")

def main():
    """Main function to either get the user's data if it is there, or store it for retrieval later."""
    path = Path('user_data.json')
    user_data = get_user_data(path)
    if user_data:
        print("This is what we know about you: ")
        for key, value in user_data.items():
            print(f"{key}: {value}")
    else:
        store_user_data(path)

# Call the main function.
if __name__ == '__main__':
    main()