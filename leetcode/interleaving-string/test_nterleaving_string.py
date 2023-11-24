from interleaving_string import Solution
import pytest


@pytest.mark.parametrize(
    ('s1', 's2', 's3', 'expected'),
    [
        ('aabcc', 'dbbca', 'aadbbcbcac', True),
        ('aabcc', 'dbbca', 'aadbbbaccc', False),
        ('', '', '', True),  # Empty strings
        ('abc', '', 'abc', True),  # One string is empty
        ('', 'abc', 'abc', True),  # One string is empty
        ('abc', 'def', 'abcdef', True),  # Non-interleaving strings
        ('abc', 'def', 'fedcba', False),  # Reversed order
        # Add more test cases as needed
    ],
)
def test_isInterleave(s1: str, s2: str, s3: str, expected: bool):
    solution = Solution()
    assert solution.isInterleave(s1, s2, s3) == expected
