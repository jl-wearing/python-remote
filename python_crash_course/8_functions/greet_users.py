# Program to greet a list of users.

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        print(f'Hello, {name.title()}')

def main():
    """Mainline logic for testing the greet_users function."""
    names = ['ronaldo', 'messi', 'nazario']
    greet_users(names)

# Call the main function.
if __name__ == '__main__':
    main()