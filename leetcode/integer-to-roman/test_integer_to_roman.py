import pytest
from integer_to_roman import Solution


@pytest.mark.parametrize(
    ["num", "expected_roman"],
    [
        [1, "I"],
        [4, "IV"],
        [9, "IX"],
        [58, "LVIII"],
        [1994, "MCMXCIV"],
        # Add more test cases as needed
    ],
)
def test_int_to_roman(num: int, expected_roman: str) -> None:
    solution = Solution()
    result = solution.intToRoman(num)
    assert result == expected_roman
