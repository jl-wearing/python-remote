import user

def main():
    """Exercise 9-3 of the textbook."""
    # Create several instances of user.
    user1 = user.User('lionel', 'messi', age=40, occupation='footballer')
    user2 = user.User('justin', 'wearing', age=24, degree='computer science', salary=1919.19)

    # Call each function on every instance.
    user1.describe_user()
    user1.greet_user()
    print(user1)
    print()
    user2.describe_user()
    user2.greet_user()
    print(user2)

# Call the main function.
if __name__ == '__main__':
    main()