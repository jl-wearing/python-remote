# Defining a function.

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

def greet_user2(username):
    """Display a simple greeting to a user."""
    print(f"Hello, {username.title()}")

def main():
    """Mainline logic to test greeting a user."""
    # Testing the greet_user() function.
    greet_user()

    # Testing the greet_user2() function.
    greet_user2('john')


if __name__ == '__main__':
    main()