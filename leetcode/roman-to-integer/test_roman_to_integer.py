import pytest
from roman_to_integer import Solution


# Test cases
@pytest.mark.parametrize(
    ["s", "expected"],
    [
        ["III", 3],
        ["LVIII", 58],
        ["I", 1],
        ["IX", 9],
        ["CDXLIV", 444],
        # Add more test cases as needed
    ],
)
def test_roman_to_int(s: str, expected: int) -> None:
    """Test the romanToInt function from the Solution class.

    Args:
    - s (str): Roman numeral input.
    - expected (int): Expected integer output.

    Returns:
    - None
    """
    solution = Solution()
    result = solution.romanToInt(s)
    assert result == expected
