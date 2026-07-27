from city_functions import get_culture


def test_city_country():
    """Tests a 'city_functions' function."""
    formatted_city = get_culture("bratislava", "slovakia", "123.999")
    assert formatted_city == "Bratislava, Slovakia\nPopulation: 123.999"
