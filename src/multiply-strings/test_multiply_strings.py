import pytest
from multiply_strings import Solution


@pytest.mark.parametrize(
    ('num1', 'num2', 'expected_output'),
    [
        ('2', '3', '6'),
        ('123', '456', '56088'),
        ('999', '999', '998001'),
        # Add more test cases as needed
    ],
)
def test_multiply(num1: str, num2: str, expected_output: str):
    solution = Solution()
    result = solution.multiply(num1, num2)
    assert result == expected_output
