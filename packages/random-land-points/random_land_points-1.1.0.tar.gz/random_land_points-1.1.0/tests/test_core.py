from random_land_points import get_resolutions

def test_resolutions():
    resolutions = get_resolutions()

    assert 'low' in resolutions
    assert 'medium' in resolutions
    assert 'high' in resolutions
    assert len(resolutions) == 3