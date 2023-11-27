import pytest
from roman_to_integer import Solution


# Test cases
@pytest.mark.parametrize(
    ["s", "expected"],
    [
        ["III", 3],  # Basic case with a simple Roman numeral.
        ["LVIII", 58],  # Complex case with a combination of Roman numerals.
        ["I", 1],  # Minimal input case.
        ["IX", 9],  # Case with subtraction (IX = 10 - 1).
        [
            "CDXLIV",
            444,
        ],  # Case with a combination of subtraction and addition.
        ["MCMXCIV", 1994],  # Case with a mix of different symbols.
        ["XC", 90],  # Case with a single subtraction (XC = 100 - 10).
        ["XL", 40],  # Another case with a single subtraction (XL = 50 - 10).
        ["CXL", 140],  # Case with multiple symbols and a subtraction.
        # Largest possible Roman numeral (MMMCMXCIX = 1000 + 1000 + 1000 - 100
        # + 100 - 10 + 9).
        [
            "MMMCMXCIX",
            3999,
        ],
        ["", 0],  # Empty string case.
        [
            "MMMMCMXCIX",
            4999,
        ],  # Case with an invalid Roman numeral (exceeds the limit of 3999).
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
