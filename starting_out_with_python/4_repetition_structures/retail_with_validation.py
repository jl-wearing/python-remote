# This program calculates retail prices.

def main():
    """Mainline logic for displaying retail prices."""
    # Constant used by the program.
    MARK_UP = 2.5

    keep_going = True
    while keep_going:
        # Input
        wholesale_cost = float(input('Enter the wholesale cost: '))

        # Validate the wholesale cost.
        while wholesale_cost < 0:
            print('ERROR: the cost cannot be negative.')
            wholesale_cost = float(input('Enter the wholesale cost: '))

        # Calculate the retail price.
        retail_price = wholesale_cost * MARK_UP

        # Display the retail price.
        print(f"Retail price: ${retail_price:.2f}")

        # Do this again?
        answer = input('Do you have another item? (y/n): ')
        if answer.lower() != 'y':
            keep_going = False

# Call the main function.
if __name__ == '__main__':
    main()