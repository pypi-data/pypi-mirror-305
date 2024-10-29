from random_land_points.countries import (
 get_country_polygons,
 get_country_points,
 get_countries
)

from random_land_points.continents import (
    get_continent_polygons,
    get_continents
)

from random_land_points.sampling import (
    random_point_in_polygon,
    random_country_points,
    random_continent_points,
    random_points,
    get_total_country_area,
    get_center_points,
    get_num_polygons,
)

from random_land_points.contains import (
    is_in,
    is_in_country,
    is_in_continent
)

def get_resolutions() -> list[str]:
    """
    Get list of valid resolutions supported by the package

    Returns:
        list[str]
            List of valid resolutions
    """
    return ['low', 'medium', 'high']