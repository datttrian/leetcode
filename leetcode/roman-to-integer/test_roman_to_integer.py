import pytest
from roman_to_integer import (
    Solution,
)  # Replace 'your_module_name' with the actual name of your module

roman_to_int = Solution().romanToInt


# Test cases
@pytest.mark.parametrize(
    ('s', 'expected'),
    [
        ('III', 3),
        ('LVIII', 58),
        ('MCMXCIV', 1994),
        # Add more test cases as needed
    ],
)
def test_roman_to_int(s: str, expected: int):
    result = roman_to_int(s)
    assert result == expected


# Additional test cases for edge cases or specific scenarios
def test_roman_to_int_edge_cases():
    # Add edge cases or specific scenarios
    assert roman_to_int('I') == 1
    assert roman_to_int('IX') == 9
    assert roman_to_int('CDXLIV') == 444
    # Add more edge cases as needed


# Run the tests
if __name__ == '__main__':
    pytest.main()
