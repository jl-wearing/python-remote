# Program to build a user profile using arbitrary keyword arguments.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

def main():
    """Mainline logic to build user profiles given any arguments provided."""
    user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
    print(user_profile)

# Call the main function.
if __name__ == '__main__':
    main()