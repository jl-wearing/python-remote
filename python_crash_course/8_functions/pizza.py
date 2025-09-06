# Program to display the toppings of a pizza being ordered.

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"\t{topping}")

def main():
    """Mainline logic for making pizzas."""
    make_pizza(25, 'tomatoes', 'extra cheese', 'mushrooms')
    make_pizza(35, 'bacon', 'macon', 'mushrooms', 'olives')

# Call the main function.
if __name__ == '__main__':
    main()