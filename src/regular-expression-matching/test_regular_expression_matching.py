import pytest
from regular_expression_matching.Solution import Solution


class TestSolution:
    @pytest.mark.parametrize(
        ('s', 'p', 'expected'),
        [
            ('aa', 'a', False),
            ('aa', 'a*', True),
            ('ab', '.*', True),
            ('aab', 'c*a*b', True),
            ('mississippi', 'mis*is*p*.', False),
        ],
    )
    def test_isMatch(self, s, p, expected):
        sol = Solution()
        result = sol.isMatch(s, p)
        assert result == expected
