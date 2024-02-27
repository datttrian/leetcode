import pytest
from minimum_window_substring import Solution


@pytest.mark.parametrize(
    ('s', 't', 'expected'),
    [
        ('ADOBECODEBANC', 'ABC', 'BANC'),
        ('a', 'a', 'a'),
        ('aa', 'aa', 'aa'),
        ('a', 'aa', ''),
        ('cabwefgewcwaefgcf', 'cae', 'cwae'),
    ],
)
def test_minWindow(s: str, t: str, expected: str):
    solution = Solution()
    result = solution.minWindow(s, t)
    assert result == expected
