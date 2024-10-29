"""
Functions related to sampling random points from polygons and
"""

import random
import numpy as np
from functools import lru_cache
from shapely.geometry import Point, Polygon
from shapely import centroid

from random_land_points.continents import get_continent_polygons, get_continents
from random_land_points.countries import get_country_polygons

def random_point_in_polygon(polygon: Polygon) -> np.ndarray:
    """
    Returns a random point within a polygon

    Args:
        polygon: np.ndarray
            The polygon to sample from

    Returns:
        np.ndarray
            The random point
    """
    min_x, min_y, max_x, max_y = polygon.bounds
    while True:
        point = np.array([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if polygon.contains(Point(point)):
            return point

@lru_cache(maxsize=10)
def compute_country_polygon_weights(country: str, resolution: str = 'medium') -> list[float]:
    """
    Compute the area weights of each polygon in a country

    Args:
        country: str
            The name of the country
        resolution:
            The resolution of the data to use. Can be 'low', 'medium', or 'high'

    Returns:
        list[float]
            The weights of each polygon
    """
    polygons = get_country_polygons(country, resolution)

    total_area = sum([polygon.area for polygon in polygons])
    return [polygon.area / total_area for polygon in polygons]

def random_country_points(country: str, count: int = 1, resolution:str = 'medium') -> list[np.ndarray]:
    """
    Returns a random point within a country

    Args:
        country: str
            The name of the country
        count: int
            The number of points to return
        resolution: str
            The resolution of the data to use. Can be 'low', 'medium', or 'high'

    Returns:
        np.ndarray
            The random point
    """

    if count < 1:
        raise ValueError("Count must be greater than 0")

    polygons = get_country_polygons(country, resolution)

    # Compute area weight of each polygon
    weights = compute_country_polygon_weights(country, resolution)

    points = []
    for _ in range(count):
        polygon = random.choices(polygons, weights=weights)[0]
        points.append(random_point_in_polygon(polygon))

    return points

@lru_cache(maxsize = 50)
def get_total_country_area(country: str, resolution: str = 'medium') -> float:
    """
    Returns the total area of a country

    Args:
        country: str
            The name of the country
        resolution: str
            The resolution of the data to use. Can be 'low', 'medium', or 'high'

    Returns:
        float
            The total area
    """

    polygons = get_country_polygons(country, resolution)
    total_area = 0
    for polygon in polygons:
        total_area += polygon.area

    return total_area

def get_num_polygons(country: str, resolution: str = 'medium') -> int:
    """
    Returns the number of polygons for a country

    Args:
        country: str
            The name of the country
        resolution: str
            The resolution of the data to use. Can be 'low', 'medium', or 'high'

    Returns:
        int
            The number of polygons
    """

    polygons = get_country_polygons(country, resolution)
    return len(polygons)

@lru_cache(maxsize = 50)
def get_center_points(country: str, resolution: str = 'medium') -> np.ndarray:
    """
    Returns the center point of a polygon

    Args:
        country: str
            The name of the country
        resolution: str
            The resolution of the data to use. Can be 'low', 'medium', or 'high'

    Returns:
        np.ndarray
            The center point
    """

    polygons = get_country_polygons(country, resolution)

    center_points = []

    for polygon in polygons:
        center_points.append(centroid(polygon).coords[0])

    return np.array(center_points)


@lru_cache(maxsize=3)
def compute_continent_polygon_weights(continent: str, resolution: str = 'medium') -> list[float]:
    """
    Compute the area weights of each polygon in a continent

    Args:
        continent: str
            The name of the continent
        resolution:
            The resolution of the data to use. Can be 'low', 'medium', or 'high'

    Returns:
        list[float]
            The weights of each polygon
    """
    polygons = get_continent_polygons(continent, resolution)

    total_area = sum([polygon.area for polygon in polygons])
    return [polygon.area / total_area for polygon in polygons]

def random_continent_points(continent: str, count: int = 1, resolution: str = 'medium') -> list[np.ndarray]:
    """
    Returns a random point within a continent

    Args:
        continent: str
            The name of the continent
        count: int
            The number of points to return
        resolution: str
            The resolution of the data to use. Can be 'low', 'medium', or 'high'

    Returns:
        np.ndarray
            The random point
    """

    if count < 1:
        raise ValueError("Count must be greater than 0")

    continent_polygons = get_continent_polygons(continent, resolution)

    # Compute area weight of each polygon - We breake this up to cache this computation for performance
    weights = compute_continent_polygon_weights(continent, resolution)

    points = []
    for _ in range(count):
        polygon = random.choices(continent_polygons, weights=weights)[0]
        points.append(random_point_in_polygon(polygon))

    return points

@lru_cache(maxsize = 7)
def get_continent_area(continent: str, resolution: str = 'medium') -> float:
    """
    Returns the total area of a continent

    Args:
        continent: str
            The name of the continent
        resolution: str
            The resolution of the data to use. Can be 'low', 'medium', or 'high'

    Returns:
        float
            The total area
    """

    polygons = get_continent_polygons(continent, resolution)
    total_area = 0
    for polygon in polygons:
        total_area += polygon.area

    return total_area

def random_points(continent: str | None = None, country: str | None = None, count: int = 1, resolution: str = 'medium') -> list[np.ndarray]:
    """
    Returns a random point on land

    Args:
        continent: str
            The name of the continent
        country: str
            The name of the country
        count: int
            The number of points to return
        resolution: str
            The resolution of the data to use. Can be 'low', 'medium', or 'high'

    Returns:
        np.ndarray
            The random point
    """

    if continent is not None and country is not None:
        raise ValueError("Only one of continent and country can be specified")

    if continent is not None:
        return random_continent_points(continent, count, resolution)
    elif country is not None:
        return random_country_points(country, count, resolution)
    else:
        # Random points anywhere on land

        if count < 1:
            raise ValueError("Count must be greater than 0")

        continent_names = get_continents(resolution)

        # Compute weight of each continent
        continent_areas = [get_continent_area(continent, resolution) for continent in continent_names]
        continent_weights = [area / sum(continent_areas) for area in continent_areas]

        points = []
        for _ in range(count):
            continent = random.choices(continent_names, weights=continent_weights)[0]
            points.append(random_continent_points(continent, 1, resolution)[0])

        return points