import os
import pytest
from pelican.themes import smallweb
from pathlib import Path


def test_path():
    theme = Path(smallweb.path())
    assert theme.exists()
    assert theme.is_dir()

    children = os.listdir(theme)
    assert 'templates' in children
    assert 'static' in children
