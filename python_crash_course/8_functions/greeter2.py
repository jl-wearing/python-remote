# Program to display a person's name, neatly formatted.

def get_formatted_name(first_name, last_name):
    """Return a person's full name, neatly formatted."""
    return f"{first_name} {last_name}".title()

def main():
    while True:
        # Input
        print('Enter (q) at any time to quit.')
        first_name = input('Input your first name: ')
        if first_name == 'q':
            break

        last_name = input('Input your last name: ')
        if last_name == 'q':
            break

        # Process
        full_name = get_formatted_name(first_name, last_name)

        # Output
        print(f"Hello, {full_name}.\n")

# Call the main function.
if __name__ == '__main__':
    main()