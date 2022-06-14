'''
Generate a custom color scheme with Pygments and convert it to CSS
'''

from pygments.style import Style
from pygments.formatters import HtmlFormatter
from pygments.token import (
        Comment,
        Error,
        Generic,
        Keyword,
        Name,
        Number,
        Operator,
        String,
)


PLACEHOLDERS = {
    # Pygments does not support CSS variables for color values, so we make do with placeholders
    '#000000': 'var(--text-color)',
    'color: #cccccc': 'opacity: 0.5',

    # Some default CSS values have to be deleted completely
    'pre { line-height: 125%; }\n': '',
}


class BleakStyle(Style):
    '''Extremely simple code highlight scheme for SmallWeb'''
    default_style = ''
    styles = {
        Comment: 'italic #cccccc',
        Keyword: 'bold',
    }


def css(style, replace=None):
    '''Convert Pygments style to CSS'''
    formatter = HtmlFormatter(style=style)
    stylesheet = formatter.get_style_defs()
    if replace is None:
        replace = PLACEHOLDERS
    for old, new in replace.items():
        stylesheet = stylesheet.replace(old, new)
    return stylesheet


def main():
    '''Print stylesheet to stdout'''
    print(css(BleakStyle))


if __name__ == '__main__':
    main()
