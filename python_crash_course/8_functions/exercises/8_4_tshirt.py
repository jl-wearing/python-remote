# Program to describe a t-shirt being made.

def make_shirt(text='I love Python', size='large'):
    """Describe a t-shirt being made."""
    print(f"You ordered a shirt of size {size}.")
    print(f"The message to be displayed on the shirt: {text}.\n")

def main():
    """Mainline logic for testing the mae_shirt function."""
    # Test with positional arguments.
    make_shirt('medium', 'It is what it is')

    # Test with keyword arguments.
    make_shirt(size='xxl', text='Python is fun!')
    make_shirt(text='Java is better tho', size='large')

    # Testing the default arguments.
    make_shirt()
    make_shirt(size='medium')

# Call the main function
if __name__ == '__main__':
    main()