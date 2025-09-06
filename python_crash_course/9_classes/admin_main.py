from user import Admin

def main():
    """Main function to test the Admin class."""
    # Create an instance of Admin.
    superuser0 = Admin('lionel', 'messi', occupation='footballer', salary=123_456_789.00)

    # Display the privileges of the admin.
    superuser0.privileges.show_privileges()


# Call the main function.
if __name__ == '__main__':
    main()