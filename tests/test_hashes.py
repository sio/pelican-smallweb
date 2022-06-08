import pytest
from pelican.themes import smallweb

def test_calculate_hashes():
    '''Check that hash calculation does not fail'''
    result = smallweb.hashes()
    assert len(result) == 2
    for value in result.values():
        assert isinstance(value, str)
        assert len(value) == 64  # sha256
