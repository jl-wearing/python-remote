import user

def main():
    """Main function."""

    # Make an instance of the user class.
    user0 = user.User('kylian', 'mbappe', location='spain', occupation='footballer')

    # Increase the login attempts several times.
    for i in range(5):
        user0.increment_login_attempts()

    # Output the number of login attempts.
    print(user0.login_attempts)

    # Reset the login attempts.
    user0.reset_login_attempts()

    # Output the number of login attempts.
    print(user0.login_attempts)

# Call the main function.
if __name__ == '__main__':
    main()