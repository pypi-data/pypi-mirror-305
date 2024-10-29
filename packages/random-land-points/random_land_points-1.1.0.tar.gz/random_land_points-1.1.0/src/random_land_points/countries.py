"""
Module that provides methods for sampling points from countires
"""

import geopandas as gpd
import numpy as np
from pathlib import Path
from shapely.geometry import MultiPolygon, Polygon
from functools import lru_cache


def get_country_data_path(resolution:str) -> Path:
    """
    Returns the path to the data file

    Args:
        resolution: str
            The resolution of the data file

    Returns:
        Path
            The path to the data file
    """

    if resolution == 'low':
        return Path(__file__).parent / 'data' / '10m' / 'ne_10m_admin_0_countries_lakes.dbf'
    elif resolution == 'medium':
        return Path(__file__).parent / 'data' / '50m' / 'ne_50m_admin_0_countries_lakes.dbf'
    elif resolution == 'high':
        return Path(__file__).parent / 'data' / '110m' / 'ne_110m_admin_0_countries_lakes.dbf'
    else:
        raise ValueError("Invalid resolution. Must be 'low', 'medium', or 'high'")

@lru_cache(maxsize = 1)
def get_country_data(resolution:str = 'medium') -> gpd.GeoDataFrame:
    """
    Returns the country data

    Args:
        resolution: str
            The resolution of the data to use. Can be 'low', 'medium', or 'high'

    Returns:
        gpd.GeoDataFrame
            The country data
    """

    return gpd.read_file(get_country_data_path(resolution))

@lru_cache(maxsize = 50)
def get_countries(resolution: str = 'medium') -> list[str]:
    """
    Returns a list of countries for which this package has country outlines of

    Returns:
        list[str]
            A list of country names
    """

    country_data = get_country_data(resolution)
    country_names = sorted(country_data['NAME_EN'].tolist())

    country_names_filtered = []

    for country in country_names:
        if country_data[country_data['NAME_EN'] == country].geometry.shape[0] >= 1:
            country_names_filtered.append(country)

    return country_names_filtered

def get_country_polygons(country: str, resolution:str = 'medium') -> list[Polygon]:
    """
    Returns the polygon of a country. May return an empty list if the country does not
    have any points at the given resolution.

    Args:
        country: str
            The name of the country
        resolution: str
            The resolution of the data to use. Can be 'low', 'medium', or 'high'

    Returns:
        np.ndarray
            The polygon of the country
    """

    countries = get_country_data(resolution)

    # Check that the continent exists
    if country not in countries['NAME_EN'].unique():
        raise ValueError(f"Country \"{country}\" does not exist")

    country_polygon = countries[countries['NAME_EN'] == country].geometry

    # Get list of numpy arrays if the country is a MultiPolygon
    if isinstance(country_polygon.iloc[0], MultiPolygon):
        polys = [poly for poly in country_polygon.iloc[0].geoms]
    else:
        polys = [country_polygon.iloc[0]]

    return polys

@lru_cache(maxsize = 50)
def get_country_points(country: str, resolution:str = 'medium') -> list[np.ndarray]:
    """
    Returns the polygon of a country. May return an empty list if the country does not
    have any points at the given resolution.

    Args:
        country: str
            The name of the country
        resolution: str
            The resolution of the data to use. Can be 'low', 'medium', or 'high'

    Returns:
        np.ndarray
            The polygon of the country
    """

    countries = get_country_data(resolution)

    # Check that the continent exists
    if country not in countries['NAME_EN'].unique():
        raise ValueError(f"Country \"{country}\" does not exist")

    country_polygon = countries[countries['NAME_EN'] == country].geometry

    # Get list of numpy arrays if the country is a MultiPolygon
    if isinstance(country_polygon.iloc[0], MultiPolygon):
        points = [np.array(poly.exterior.coords) for poly in country_polygon.iloc[0].geoms]
    else:
        points = [np.array(country_polygon.iloc[0].exterior.coords)]

    return points
