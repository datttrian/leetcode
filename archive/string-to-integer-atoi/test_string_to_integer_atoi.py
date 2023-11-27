import pytest
from string_to_integer_atoi import Solution


@pytest.mark.parametrize(
    ('input_str', 'expected_output'),
    [
        ('42', 42),
        ('   -42', -42),
        ('4193 with words', 4193),
        ('words and 987', 0),
        ('-91283472332', -2147483648),
        ('', 0),
        ('    ', 0),
        ('+1', 1),
        ('2147483648', 2147483647),  # Overflow case
        ('-2147483649', -2147483648),  # Underflow case
    ],
)
def test_myAtoi(input_str: str, expected_output: int):
    solution = Solution()
    assert solution.myAtoi(input_str) == expected_output
