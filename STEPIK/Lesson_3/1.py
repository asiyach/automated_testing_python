
def test_substring(full_string, substring):
    assert (substring in full_string), f'expected {substring} to be substring of {full_string}'

# expected 'some_value' to be substring of 'fulltext'
#     assert (full_string in substring), f'expected {full_string} to be substring of {substring} '
