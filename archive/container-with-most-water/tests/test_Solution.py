import pytest
from container_with_most_water.Solution import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "height, expected",
        [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([4, 3, 2, 1, 4], 16), ([1, 2, 1], 2)],
    )
    def test_maxArea(self, height, expected):
        solution = Solution()
        assert solution.maxArea(height) == expected
