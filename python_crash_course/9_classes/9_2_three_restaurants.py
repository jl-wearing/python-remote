import restaurant as rt

def main():
    """Exercise 9-2 from the textbook."""
    # Create 3 different instances of restaurant.
    nandos = rt.Restaurant('nandos', 'chicken')
    chicken_licken = rt.Restaurant('chicken licken', 'chicken')
    braai_place = rt.Restaurant('braai place', 'beef')

    # Call describe_restaurant() for each instance.
    restaurants = [nandos, chicken_licken, braai_place]
    for restaurant in restaurants:
        restaurant.describe_restaurant()

# Call the main function.
if __name__ == '__main__':
    main()