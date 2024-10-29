"""
Module that provides methods for sampling points from continents
"""

from shapely.geometry import MultiPolygon, Polygon
from functools import lru_cache

from random_land_points.countries import get_country_data


@lru_cache(maxsize = 1)
def get_continents(resolution: str = 'medium') -> list[str]:
    """
    Returns a list of continents for which this package has continent outlines of

    Returns:
        list[str]
            A list of continent names
    """

    continent_data = get_country_data(resolution)
    continent_names = sorted(continent_data['CONTINENT'].unique())

    # Remove "Seven seas (open ocean)"
    continent_names.remove('Seven seas (open ocean)')

    return continent_names

@lru_cache(maxsize=7)
def get_continent_polygons(continent: str, resolution: str = 'medium') -> list[Polygon]:
    """
    Returns a dictionary of continent names to their polygons

    Returns:
        dict[str, Polygon]
            A dictionary of continent names to their polygons
    """

    countries = get_country_data(resolution)

    # Check that the continent exists
    if continent not in countries['CONTINENT'].unique():
        raise ValueError(f"Continent \"{continent}\" does not exist")

    country_polygon = countries[countries['CONTINENT'] == continent].geometry

    polys = []

    for i in range(country_polygon.shape[0]):
        if isinstance(country_polygon.iloc[i], MultiPolygon):
            polys.extend([poly for poly in country_polygon.iloc[i].geoms])
        else:
            polys.append(country_polygon.iloc[i])

    return polys
