def city_country(city: str, country: str, population=None) -> str:
    """Function to return a city and country, neatly formatted."""
    if not population:
        return f"{city}, {country}".title()
    return f"{city}, {country} population - {population:,}".title()