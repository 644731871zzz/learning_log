from city_functions import city_and_country

def test_city_and_contry():
    city_country=city_and_country('shanghai', 'china',30000000)
    assert city_country=="Shanghai, China - Population 30000000"