# Program to display a count-down.

def main():
    """Main function."""
    print('Beginning countdown.')
    count = 10
    while count >= 0:
        print(count, end=' ')
        count -= 1

# Call the main function.
if __name__ == '__main__':
    main()