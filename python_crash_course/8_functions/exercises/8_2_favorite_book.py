# exercise 8-2

def favorite_book(title):
    """Display what a person's favorite book is."""
    print(f'One of my favorite books is {title.title()}.')

def main():
    """Mainline logic to test the favorite_book function."""
    favorite_book('python crash course')
    favorite_book('Alice in Wonderland')

# Call the main function.
if __name__ == '__main__':
    main()