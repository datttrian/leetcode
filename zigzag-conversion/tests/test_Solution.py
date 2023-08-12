import pytest
from zigzag_conversion.Solution import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "s, numRows, expected",
        [
            ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
            ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
            ("A", 1, "A"),
            ("AB", 1, "AB"),
            ("ABC", 2, "ACB"),
            ("ABCDE", 4, "ABCED"),
        ],
    )
    def test_convert(self, s, numRows, expected):
        solution = Solution()
        assert solution.convert(s, numRows) == expected
