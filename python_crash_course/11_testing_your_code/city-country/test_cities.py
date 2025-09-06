from city_functions import city_country

def test_city_country():
    """Do pairs like 'Santiago, Chile' work?"""
    formatted_city_country = city_country('santiago', 'chile')
    assert formatted_city_country == 'Santiago, Chile'

def test_city_country_population():
    """Do triplets like 'Santiago, Chile Population - 10000' work?"""
    formatted_city_country_population = city_country('santiago', 'chile', 10000)
    assert formatted_city_country_population == 'Santiago, Chile Population - 10,000'