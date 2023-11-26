import pytest
from integer_to_roman import (  # Assuming your solution is in a module named solution_module
    Solution,
)


@pytest.mark.parametrize(
    ('num', 'expected_roman'),
    [
        (1, 'I'),
        (4, 'IV'),
        (9, 'IX'),
        (58, 'LVIII'),
        (1994, 'MCMXCIV'),
        # Add more test cases as needed
    ],
)
def test_intToRoman(num: int, expected_roman: str):
    solution = Solution()
    result = solution.intToRoman(num)
    assert result == expected_roman
