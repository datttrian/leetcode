import pytest
from scramble_string import Solution


@pytest.mark.parametrize(
    ('s1', 's2', 'expected_result'),
    [
        # Test case with valid scramble
        ('great', 'rgeat', True),
        # Test case with invalid scramble
        ('abcde', 'caebd', False),
        # Test case with empty strings
        # ('', '', True),
        # Test case with single-character strings
        ('a', 'a', True),
        ('a', 'b', False),
        # Test case with repeated characters
        ('abb', 'bab', True),
        ('abb', 'bba', True),
        ('abc', 'bca', True),
        # Test case with different lengths
        ('abcd', 'abc', False),
        ('abcd', 'abdc', True),
    ],
)
def test_isScramble(s1: str, s2: str, expected_result: bool):
    solution = Solution()
    result = solution.isScramble(s1, s2)
    assert result == expected_result
