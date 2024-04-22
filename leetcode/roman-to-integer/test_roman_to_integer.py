import pytest
from roman_to_integer import Solution


@pytest.mark.parametrize(
    ["s", "expected"],
    [
        ["III", 3],
        ["LVIII", 58],
        ["I", 1],
        ["IX", 9],
        [
            "CDXLIV",
            444,
        ],
        ["MCMXCIV", 1994],
        ["XC", 90],
        ["XL", 40],
        ["CXL", 140],
        [
            "MMMCMXCIX",
            3999,
        ],
        ["", 0],
    ],
)
def test_roman_to_int(s: str, expected: int) -> None:
    solution = Solution()
    result = solution.romanToInt(s)
    assert result == expected
