# Basic theme setup
from pelican.themes import smallweb
THEME = smallweb.path()

# Custom color scheme (optional)
import os
accent = os.getenv('SMALLWEB_ACCENT')
print(f'Rendering demo with accent color: {accent}')
if accent:
    SMALLWEB_COLORS = smallweb.colors(accent)

# Automatic cache invalidation for static files (optional)
SMALLWEB_HASHES = smallweb.hashes()


# Some obligatory Pelican configuration
LOCALE = 'C'
DEFAULT_CATEGORY = 'posts'
DEFAULT_LANG = 'EN'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
MENUITEMS = [
    ('github', 'https://github.com/sio/pelican-smallweb'),
    ('pypi', 'https://pypi.org/project/pelican-theme-smallweb/'),
    ('pelican', 'https://getpelican.com/'),
]
