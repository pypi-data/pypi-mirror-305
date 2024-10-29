"""
This module contains functions to test whether a given point is contained within the respective generating land pass
"""
import numpy as np
from shapely.geometry import Point, Polygon

from random_land_points.continents import get_continent_polygons, get_continents
from random_land_points.countries import get_country_polygons

def _is_in_polygon(point: np.ndarray | list[float] | list[int], polygons: list[Polygon]) -> bool:
    """
    Returns whether a point is contained within a list of input polygons.

    This is an internal function and should not be called directly.

    Args:
        point: np.ndarray | list[float] | list[int]
        polygons: list[Polygon]

    Returns:
        bool
    """
    if not isinstance(point, np.ndarray):
        point = np.array(point) # Coerce type

    p = point.reshape(-1)


    if p.shape[0] != 2:
        raise ValueError(f'Input point must be a 2D Vector. Found {p.shape[0]}')

    p = Point(p[0], p[1])

    # Check if point is in every potential polygon
    for poly in polygons:
        if poly.contains(p):
            # Return early to possibly same some checks if we find it early
            return True

    return False

def is_in_continent(point: np.ndarray | list[float] | list[int], continent: str, resolution: str = 'medium') -> bool:
    """
    Returns whether a point is contained within a given continent.

    Args:
        point: np.ndarray | list[float] | list[int]
            The point to check
        continent: str
            The continent to check against
        resolution: str
            The resolution of the data to use. Can be 'low', 'medium', or 'high'

    Returns:
        bool
            Whether the point is contained in the continent
    """

    # Get Country polygons
    polygons = get_continent_polygons(continent, resolution)

    return _is_in_polygon(point, polygons)

def is_in_country(point: np.ndarray | list[float] | list[int], country: str, resolution: str = 'medium') -> bool:
    """
    Returns whether a point is contained within a given country.

    Args:
        point: np.ndarray | list[float] | list[int]
            The point to check
        country: str
            The country to check against
        resolution: str
            The resolution of the data to use. Can be 'low', 'medium', or 'high'

    Returns:
        bool
            Whether the point is contained in the country
    """

    # Get Country polygons
    polygons = get_country_polygons(country, resolution)

    return _is_in_polygon(point, polygons)

def is_in(point: np.ndarray | list[float] | list[int], continent: str | None = None, country: str | None = None, resolution: str = 'medium') -> bool:
    """
    Returns whether a point is contained within a sampling region. This can be a continent or a country, or if neither
    are specified, all land.

    Args:
        point: np.ndarray | list[float] | list[int]
            The point to check
        continent: str | None
            The continent to check against
        country: str | None
            The country to check against
        resolution: str
            The resolution of the data to use. Can be 'low', 'medium', or 'high'

    Returns:
        bool
            Whether the point is contained in the region
    """

    if continent is not None and country is not None:
        raise ValueError("Only one of continent and country can be specified")

    if continent is not None:
        return is_in_continent(point, continent, resolution)
    elif country is not None:
        return is_in_country(point, country, resolution)
    else:
        # Ensure point is right shape and format
        if not isinstance(point, np.ndarray):
            point = np.array(point)  # Coerce type
        p = point.reshape(-1).squeeze()

        if p.shape[0] != 2:
            raise ValueError(f'Input point must be a 2D Vector. Found {p.shape[0]}')

        p = Point(p[0], p[1])

        continent_names = get_continents(resolution)

        # Check all possible continents for being contained in for thoroughness.
        # This could be improved by using pre-defined heuristics to know which continents to
        # check
        for cname in continent_names:
            for cpolygon in get_continent_polygons(cname, resolution):
                if cpolygon.contains(p):
                    return True

        return False