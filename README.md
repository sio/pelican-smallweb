# SmallWeb theme for Pelican static site generator

This is a simple yet modern-looking theme for Pelican blogs. It uses no
JavaScript, and all HTML/CSS had been crafted by hand - remember [webmasters]?

Theme name is inspired by the idea of [small web] - a simpler old-style web of
personal pages that didn't actually disappear but has become a lot less
visible as Internet had grown older and larger.
Authors would like to thank [Marginalia Search] for keeping the spirit alive!

[webmasters]: https://justinjackson.ca/webmaster/
[small web]: https://felix.plesoianu.ro/web/in-the-small.html
[Marginalia Search]: https://search.marginalia.nu/


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


## Privacy concerns

This theme uses *Google Fonts* by default. If you do not want third-parties to
track your visitors, set `ALLOW_GOOGLE_FONTS = False` in your pelicanconf.py
and (optionally) provide self-hosted version of fonts via `CSS_OVERRIDE` list.

No other third-party resources are referenced.

No personally identifiable information is collected.
