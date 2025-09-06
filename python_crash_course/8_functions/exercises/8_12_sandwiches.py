# Program to build a sandwich and display the contents.

def make_sandwich(*toppings):
    """Build a sandwich a person wants."""
    print('\nMaking a sandwich with the following toppings:')
    for topping in toppings:
        print(f'Adding:\t{topping.lower()}')

def main():
    """Mainline logic for making sandwiches."""
    make_sandwich('margarine', 'egg', 'bacon', 'lettuce')
    make_sandwich('lettuce', 'patty', 'tomato')
    make_sandwich('butter', 'peanut butter', 'jam')

# Call the main function.
if __name__ == '__main__':
    main()