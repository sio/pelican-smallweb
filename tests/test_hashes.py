import pytest
from pelican.themes import smallweb

def test_calculate_hashes():
    '''Check that hash calculation does not fail'''
    result = smallweb.hashes()
    assert len(result) >= 2
    for key, value in result.items():
        assert key.startswith('/')
        assert key.endswith('.css')
        assert isinstance(value, str)
        assert len(value) == 64  # sha256
