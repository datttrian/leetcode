import pytest
from length_of_last_word import Solution


@pytest.mark.parametrize(
    ('s', 'expected'),
    [
        ('Hello World', 5),
        ('   Hello   World   ', 5),
        ('   Hello', 5),
        ('Hello', 5),
        ('', 0),
        ('   ', 0),
        ('Word', 4),
        ('Spaces Before and After  ', 5),
        ('One', 3),
        ('  One   ', 3),
        ('  One  Two   ', 3),
        ('   One Two Three   ', 5),
        ('  ', 0),
    ],
)
def test_lengthOfLastWord(s: str, expected: int):
    solution = Solution()
    result = solution.lengthOfLastWord(s)
    assert result == expected
