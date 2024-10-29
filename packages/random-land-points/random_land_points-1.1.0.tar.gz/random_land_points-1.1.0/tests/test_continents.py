import pytest
from random_land_points.continents import get_continents, get_continent_polygons

def test_get_continents():
    continents = get_continents()

    assert 'Africa' in continents
    assert 'Asia' in continents
    assert 'Europe' in continents
    assert 'North America' in continents
    assert 'Oceania' in continents
    assert 'South America' in continents
    assert 'Antarctica' in continents
    assert(len(continents) == 7)

def test_get_continent_polygons():
    for continent in get_continents():
        polygons = get_continent_polygons(continent)
        assert len(polygons) > 0

def test_get_continent_name_invalid():

    # Confirm raises ValueError
    with pytest.raises(ValueError):
        get_continent_polygons('Not a continent')