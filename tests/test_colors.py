'''
Test color conversion functions
'''


import pytest
from pelican.themes import smallweb


@pytest.mark.parametrize('color,expected', [
        ('#00bfff', (195, 100, 50)),
        ('#00BFFF', (195, 100, 50)),
        ('00BFFF',  (195, 100, 50)),
        ('#ff0000', (0, 100, 50)),
        ('#00ff00', (120, 100, 50)),
        ('#0000ff', (240, 100, 50)),
        ('#000000', (0, 0, 0)),
        ('#ffffff', (0, 0, 100)),
        ('#f26a3d', (15, 87, 59)),
    ])
def test_color_rgb(color, expected):
    result = smallweb._rgb2hsl(color)
    assert expected == tuple(round(i, 0) for i in result), result
