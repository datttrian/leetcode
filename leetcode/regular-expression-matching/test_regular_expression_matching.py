import pytest
from regular_expression_matching import Solution


@pytest.mark.parametrize(
    ('s', 'p', 'expected'),
    [
        ('aa', 'a', False),
        ('aa', 'a*', True),
        ('ab', '.*', True),
        ('aab', 'c*a*b', True),
        ('mississippi', 'mis*is*p*.', False),
    ],
)
def test_isMatch(s: str, p: str, expected: bool):
    sol = Solution()
    result = sol.isMatch(s, p)
    assert result == expected
