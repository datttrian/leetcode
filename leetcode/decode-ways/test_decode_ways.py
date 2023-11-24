import pytest
from decode_ways import Solution


@pytest.mark.parametrize(
    ('s', 'expected_result'),
    [
        ('12', 2),
        ('226', 3),
        ('0', 0),
        ('06', 0),
        ('10', 1),
        ('2101', 1),
        ('27', 1),
        ('11106', 2),
        # Add more test cases as needed
    ],
)
def test_numDecodings(s: str, expected_result: int):
    solution = Solution()
    result = solution.numDecodings(s)
    assert result == expected_result
