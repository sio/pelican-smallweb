# SmallWeb theme for Pelican static site generator

This is a simple yet modern-looking theme for Pelican blogs. It uses no
JavaScript, and all HTML/CSS had been crafted by hand - remember [webmasters]?

Theme name is inspired by the idea of [small web] - a simpler old-style web of
personal pages that didn't actually go anywhere but has become a lot less
visible as Internet had grown older and larger.

[webmasters]: https://justinjackson.ca/webmaster/
[small web]: https://felix.plesoianu.ro/web/in-the-small.html


## Installation and usage

This theme is installable via pip:

```
$ pip install git+https://github.com/sio/pelican-smallweb/
```

Import it in your `pelicanconf.py`:

```python
from pelican.themes import smallweb
THEME = smallweb.path()
```
