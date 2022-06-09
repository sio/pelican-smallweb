date: 2022-06-10
title: SmallWeb: changing color scheme
tags: smallweb, demo

You can color your site differently from the default palette, use any accent
you like:

- [Default colors][default]
- [`accent='#ff0000'`][red]
- [`accent='#0000ff'`][blue]

[SmallWeb]: https://github.com/sio/pelican-smallweb
[default]: https://sio.github.io/pelican-smallweb/default/
[red]: https://sio.github.io/pelican-smallweb/red/
[blue]: https://sio.github.io/pelican-smallweb/blue/

[SmallWeb] uses CSS variables to build the palette:

```css
:root {
  --accent-color:  hsl(
    var(--accent-hue),
    var(--accent-saturation),
    var(--accent-lightness)
  ); /* rgb(242,106,61) */
  --accent-color-darker: hsl(
    var(--accent-hue),
    calc(var(--accent-saturation) - 27.9%),
    calc(var(--accent-lightness) - 11.9%)
  );
  --accent-hue: 15; /* TODO: convert from RGB in theme variables */
  --accent-saturation: 87.4%;
  --accent-lightness: 59.4%;

  --text-color: black;
  --text-color-inverted: white;
  --page-color: white;
}
```

You can override these via `CSS_OVERRIDE` or `SMALLWEB_COLORS` to provide your own color scheme.

There is also a convenient Python function that generates the color scheme and
handles RGB to HSL color space conversion automatically:

```python
# add to your pelicanconf.py
SMALLWEB_COLORS = smallweb.colors(accent='#ff0000')
```
