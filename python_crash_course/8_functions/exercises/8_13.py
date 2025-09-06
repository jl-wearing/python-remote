def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

def main():
    """Mainline logic for building user profiles."""
    profile = build_profile('lionel', 'messi', occupation='footballer', salary=1_000_000.00, location='miami')
    # Output
    print(profile)

# Call the main function.
if __name__ == '__main__':
    main()