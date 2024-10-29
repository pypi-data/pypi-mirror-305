import pytest

from random_land_points import is_in_continent, is_in_country, is_in

from random_land_points.continents import get_continents
from random_land_points.countries import get_countries
from random_land_points.sampling import random_points

def test_is_in_continent():

    # Sample from every continent, confirm sampled point is in that continent
    for continent in get_continents():
        point = random_points(continent=continent)[0]
        assert is_in_continent(point, continent)

def test_is_in_country():

    # Sample from every country, confirm sampled point is in that country
    for country in get_countries():
        point = random_points(country=country)[0]
        assert is_in_country(point, country)

def test_is_in_base():
    # Test is_in without arguments
    point = random_points()[0]
    assert is_in(point)

def test_is_in_continent_arg():

    # Test is_in with continent argument
    for continent in get_continents():
        point = random_points(continent=continent)[0]
        assert is_in(point, continent=continent)

def test_is_in_country_arg():

    # Test is_in with country argument
    for country in get_countries():
        point = random_points(country=country)[0]
        assert is_in(point, country=country)

def test_is_in_bad_input():
    with pytest.raises(ValueError):
        is_in([0, 0], continent='Asia', country='United States of America')

def test_is_in_bad_len_input():
    with pytest.raises(ValueError):
        is_in([0, 0, 0, 0])

def test_is_in_country_bad_len_input():
    with pytest.raises(ValueError):
        is_in_country([0, 0, 0], country='Italy')

def test_is_in_list_input():
    assert is_in([0, 0]) == False

def test_is_in_country_list_input():
    assert is_in([0, 0], country='United States of America') == False


def test_is_in_continent_list_input():
    assert is_in([0, 0], continent='Asia') == False