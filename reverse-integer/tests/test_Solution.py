import pytest
from reverse_integer.Solution import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "x, expected",
        [
            (123, 321),
            (-123, -321),
            (120, 21),
            (0, 0),
            (1534236469, 0),
        ],
    )
    def test_reverse(self, x, expected):
        solution = Solution()
        assert solution.reverse(x) == expected
