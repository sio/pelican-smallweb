title: SmallWeb: installation and usage
date: 2022-06-09
tags: pelican, smallweb, theme

This theme is installable via [PyPI]:

```
$ pip install pelican-theme-smallweb
```

Latest development version is also installable:

```
$ pip install git+https://github.com/sio/pelican-smallweb/
```

Import it in your `pelicanconf.py`:

```python
from pelican.themes import smallweb
THEME = smallweb.path()
```

[PyPI]: https://pypi.org/project/pelican-theme-smallweb/
