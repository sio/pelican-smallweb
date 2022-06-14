'''
SmallWeb theme for Pelican static site generator
'''

import colorsys
from collections import namedtuple
from pkg_resources import resource_filename, resource_string, resource_listdir, resource_isdir
from hashlib import sha256 as hashfunc

def path():
    '''
    Return path to theme templates and assets
    Use this as value for THEME in Pelican settings
    '''
    return resource_filename(__name__, '')


def hashes():
    '''Return hashes of static resources'''
    prefix = 'static'
    return {
        name.replace(f'{prefix}', '', 1): _hash(name)
        for name in _static_resources(prefix)
    }
def _hash(filename):
    checksum = hashfunc(resource_string(__name__, filename))
    return checksum.hexdigest()
def _static_resources(path):
    for name in resource_listdir(__name__, path):
        resource = f'{path}/{name}'
        if resource_isdir(__name__, resource):
            yield from _static_resources(path=resource)
        else:
            yield resource


PALETTE = dict(
    default = "#f26a3d",
    purple = "#6d82ee",
    green = "#7ae17f",
)
RGB = namedtuple('RGB', ['red', 'green', 'blue'])
HSL = namedtuple('HSL', ['hue', 'saturation', 'lightness'])
def _rgb2hsl(color_hex: str):
    color_hex = color_hex.strip('#')
    rgb_hex = RGB(*(color_hex[:2], color_hex[2:4], color_hex[4:6]))
    rgb_int = RGB(*(int(f'0x{v}', base=16) for v in rgb_hex))
    rgb = RGB(*(v/255.0 for v in rgb_int))
    hue, lightness, saturation = colorsys.rgb_to_hls(*rgb)
    hsl = HSL(hue * 360, saturation * 100, lightness * 100)
    return hsl
def colors(accent="#f26a3d"):
    '''Generate color pallette for CSS'''
    accent = _rgb2hsl(accent)
    palette = dict()
    palette['accent-hue'] = accent.hue
    palette['accent-saturation'] = f'{accent.saturation}%'
    palette['accent-lightness'] = f'{accent.lightness}%'
    return palette
