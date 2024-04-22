import pytest
from integer_to_roman import Solution


@pytest.mark.parametrize(
    ["num", "expected_roman"],
    [
        [3, "III"],
        [58, "LVIII"],
        [1, "I"],
        [9, "IX"],
        [444, "CDXLIV"],
        [1994, "MCMXCIV"],
        [90, "XC"],
        [40, "XL"],
        [140, "CXL"],
        [3999, "MMMCMXCIX"],
        [0, ""],
    ],
)
def test_int_to_roman(num: int, expected_roman: str) -> None:
    solution = Solution()
    result = solution.intToRoman(num)
    assert result == expected_roman
