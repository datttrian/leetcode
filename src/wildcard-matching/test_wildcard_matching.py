import pytest
from wildcard_matching import Solution


@pytest.mark.parametrize(
    ('s', 'p', 'expected'),
    [
        ('aa', 'a', False),
        ('aa', '*', True),
        ('cb', '?a', False),
        ('adceb', '*a*b', True),
        ('acdcb', 'a*c?b', False),
        ('', '', True),
        ('abc', '', False),
        ('', '*', True),
        ('abc', '****', True),
        ('abc', '*?*', True),
        # ('abc', '*?a', False),
        ('abc', '*?d', False),
        ('abc', '*?*d', False),
        ('abc', '*?*c', True),
        ('abc', '*?*a', True),
        ('abc', 'a?c', True),
    ],
)
def test_isMatch(s: str, p: str, expected: bool):
    solution = Solution()
    assert solution.isMatch(s, p) == expected
