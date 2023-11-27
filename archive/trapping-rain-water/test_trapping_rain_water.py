from typing import List

import pytest
from trapping_rain_water import Solution


@pytest.mark.parametrize(
    ('height', 'expected_output'),
    [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        # Add more test cases as needed
    ],
)
def test_trap(height: List[int], expected_output: int):
    solution = Solution()
    result = solution.trap(height)
    assert result == expected_output
