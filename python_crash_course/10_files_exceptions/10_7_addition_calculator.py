# Program to add 2 numbers continuously.

def main():
    """Main function for adding 2 numbers."""
    print('\nInput 2 numbers and I will add them.')
    print("Enter 'q' to quit.")
    while True:
        first_number = input('First number: ')
        if first_number == 'q':
            break

        second_number = input('Second number: ')
        if second_number == 'q':
            break

        try:
            answer = int(first_number) + int(second_number)
        except ValueError:
            print('Please enter two numbers.')
        else:
            print(f"{first_number} + {second_number} = {answer}")

# Call the main function.
if __name__ =='__main__':
    main()