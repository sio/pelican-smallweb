'''
SmallWeb theme for Pelican static site generator
'''

from pkg_resources import resource_filename, resource_string
from hashlib import sha256 as hashfunc

def path():
    '''
    Return path to theme templates and assets
    Use this as value for THEME in Pelican settings
    '''
    return resource_filename(__name__, '')


RESOURCES = [
    '/css/fonts.css',
    '/css/style.css',
]
def hashes():
    return {name: _hash('static' + name) for name in RESOURCES}



def _hash(filename):
    checksum = hashfunc(resource_string(__name__, filename))
    return checksum.hexdigest()
