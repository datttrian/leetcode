import pytest
from valid_number import Solution


@pytest.mark.parametrize(
    ('input_str', 'expected_result'),
    [
        # Valid integers
        ('0', True),
        ('123', True),
        ('-456', True),
        # Valid decimals
        ('0.5', True),
        ('-0.5', True),
        ('123.456', True),
        # Valid exponentials
        ('1e10', True),
        ('-2E-5', True),
        # Valid combinations
        ('3.14e-2', True),
        ('-7.89E6', True),
        # Invalid strings
        ('abc', False),
        ('1.2.3', False),
        ('1e2e3', False),
        ('1e', False),
        ('e3', False),
        ('+', False),
        ('-.', False),
        ('', False),
    ],
)
def test_isNumber(input_str: str, expected_result: bool):
    solution = Solution()
    assert solution.isNumber(input_str) == expected_result
