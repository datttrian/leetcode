import pytest
from maximal_rectangle import Solution


@pytest.mark.parametrize(
    ('matrix', 'expected_result'),
    [
        # Test case with maximal rectangles
        (
            [
                ['1', '0', '1', '0', '0'],
                ['1', '0', '1', '1', '1'],
                ['1', '1', '1', '1', '1'],
                ['1', '0', '0', '1', '0'],
            ],
            6,
        ),
        # Test case with no rectangles
        (
            [
                ['0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0'],
            ],
            0,
        ),
        # Test case with an empty matrix
        ([], 0),
        # Test case with a single row
        (
            [
                ['1', '0', '1', '0', '0'],
            ],
            1,
        ),
        # Test case with a single column
        (
            [
                ['1'],
                ['0'],
                ['1'],
                ['0'],
                ['0'],
            ],
            1,
        ),
    ],
)
def test_maximalRectangle(matrix: list[list[str]], expected_result: int):
    solution = Solution()
    result = solution.maximalRectangle(matrix)
    assert result == expected_result
