def get_formatted_name(first: str, last: str, middle='') -> str:
    """Generate a neatly formatted full name."""
    if middle:
        return f"{first} {middle} {last}".title()
    return f"{first} {last}".title()

def main():
    """Main function to test the get_formatted_name() function."""
    print("Enter 'q' at any time to quit.")
    while True:
        first = input('Please give me a first name: ')
        if first.lower() == 'q':
            break

        last = input('Please give me a last name: ')
        if last.lower() == 'q':
            break

        formatted_name = get_formatted_name(first, last)
        print(f"\nNeatly formatted name: {formatted_name}")

# Call the mai function.
if __name__ == '__main__':
    main()