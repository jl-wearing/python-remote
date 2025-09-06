# Program to describe a city in a country.

def describe_city(city, country='South Africa'):
    """Display the country a city is in."""
    print(f"{city.title()} is in {country.title()}.")

def main():
    """Mainline logic to test the describe_city function."""
    # Test with 3 cities, one of which is not in the default country.
    describe_city('Johannesburg')
    describe_city('New York', 'United States')
    describe_city('abuja')

# Call the main function.
if __name__ == '__main__':
    main()