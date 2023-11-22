import pytest
from edit_distance import Solution


@pytest.mark.parametrize(
    ('word1', 'word2', 'expected'),
    [
        ('horse', 'ros', 3),  # Replace 'h' with 'r', delete 'o', delete 'e'
        # Replace 'i' with 'e', insert 'u', replace 'n' with 'x', insert 'c',
        # insert 'u'
        (
            'intention',
            'execution',
            5,
        ),
        (
            'abc',
            'def',
            3,
        ),  # Replace 'a' with 'd', replace 'b' with 'e', replace 'c' with 'f'
        (
            'kitten',
            'sitting',
            3,
        ),  # Replace 'k' with 's', replace 'i' with 'i', insert 'g'
        ('', 'word', 4),  # Insert 'w', insert 'o', insert 'r', insert 'd'
        ('abc', '', 3),  # Delete 'a', delete 'b', delete 'c'
        ('', '', 0),  # Both strings are empty, no operations needed
    ],
)
def test_minDistance(word1: str, word2: str, expected: int):
    solution = Solution()
    result = solution.minDistance(word1, word2)
    assert result == expected
