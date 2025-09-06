# Program to return a city and its country, neatly formatted.

def city_country(city, country):
    """Return a city and its country, neatly formatted."""
    return f"{city}, {country}".title()

def main():
    """Mainline logic to test the city_country function."""
    # Test the function with at least 3 different city-country pairs.
    data1 = city_country("New York", "US")
    data2 = city_country(country='Chile', city='Santiago')
    data3 = city_country(city='cape town', country='south africa')

    # Output
    print(data1, data2, data3, sep='\n')

# Call the main function.
if __name__ == '__main__':
    main()