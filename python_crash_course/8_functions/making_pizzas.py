import pizza

def main():
    """Main function for making pizzas."""
    pizza.make_pizza(15, 'pepperoni')
    pizza.make_pizza(15, 'mushrooms', 'bacon', 'ground beef')

# Call the main function.
if __name__ == '__main__':
    main()