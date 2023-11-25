import pytest
from roman_to_integer import Solution


# Test cases
@pytest.mark.parametrize(
    ('s', 'expected'),
    [
        ('III', 3),
        ('LVIII', 58),
        ('I', 1),
        ('IX', 9),
        ('CDXLIV', 444),
        # Add more test cases as needed
    ],
)
def test_roman_to_int(s: str, expected: int):
    solution = Solution()
    result = solution.romanToInt(s)
    assert result == expected
