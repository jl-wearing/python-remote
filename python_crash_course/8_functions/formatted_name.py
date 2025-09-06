# Program to format a person's name.

def get_formatted_name(first_name, last_name, middle_name=''):
    """Display a person's name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

def main():
    """Testing the get_formatted_name function."""
    name1 = get_formatted_name("John", "Smith")
    name2= get_formatted_name('lionel', 'messi')

    # Output
    print(name1, name2, sep='\n')

    # Testing the function with a middle name.
    full_name = get_formatted_name('Justin', 'Wearing', 'Leon')

    # Output
    print(full_name)

# Call the main function.
if __name__ == '__main__':
    main()