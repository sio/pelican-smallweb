'''
Fetch fonts for this theme
'''

import argparse
import logging
from pathlib import Path
from textwrap import dedent
from urllib.request import urlretrieve

import toml


CSS = dedent('''
    @font-face {{
        font-family: '{family}';
        font-style: {style};
        font-weight: {weight};
        src: {locals_}, {remotes};
    }}
''')


logging.basicConfig(level=logging.INFO, format='%(levelname)-8s %(message)s')
log = logging.getLogger(__name__)


def main(*a, **ka):
    args = parse_args(*a, **ka)
    with args.config.open() as f:
        config = toml.load(f)
    styles = []
    for name, font in config.items():
        fetch(font, name, args.dest)
        styles.append(stylesheet(font, name))
    with (args.dest / 'static' / 'css' / 'fonts.css').open('w') as css:
        css.write('\n'.join(styles))
        log.info(f'Stylesheet created: {css.name}')


def fetch(font, name, dest):
    for filetype, url in font['remote'].items():
        filename = dest / 'static' / 'fonts' / f'{name}.{filetype}'
        urlretrieve(url, filename)
        log.info(f'Saved font: {filename.resolve()}')


def stylesheet(font, name):
    remotes = []
    for filetype in font['remote']:
        url = f'/theme/fonts/{name}.{filetype}'  # TODO: use {{ THEME_STATIC_DIR }} instead of hardcoded 'theme'
        remotes.append(f'url("{url}") format("{filetype}")')
    return CSS.format(
        family=font['family'],
        style=font.get('style', 'normal'),
        weight=font.get('weight', 400),
        locals_=', '.join(f'local("{name}")' for name in font['local']),
        remotes=', '.join(remotes)
    )


def parse_args(*a, **ka):
    parser = argparse.ArgumentParser(
        description='Fetch fonts prior to building SmallWeb theme',
    )
    parser.add_argument(
        'dest',
        metavar='DEST',
        help='Pelican theme directory',
        type=Path,
    )
    parser.add_argument(
        '--config',
        metavar='TOML',
        help='Configuration file in TOML format',
        default='fonts.toml',
        type=Path,
    )
    args = parser.parse_args(*a, **ka)
    if not args.config.exists():
        parser.error(f'Configuration file not found: {args.config.resolve()}')
    if not args.dest.exists():
        parser.error(f'Directory does not exist: {args.dest.resolve()}')
    if args.dest.is_file():
        parser.error(f'File exists instead of directory: {args.dest.resolve()}')
    return args


if __name__ == '__main__':
    main()
