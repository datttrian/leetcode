import pytest
from subsets_ii import Solution


@pytest.mark.parametrize(
    ('nums', 'expected_result'),
    [
        (
            [1, 2, 2],
            [
                [],
                [1],
                [1, 2],
                [1, 2, 2],
                [2],
                [2, 2],
            ],
        ),
        (
            [0],
            [
                [],
                [0],
            ],
        ),
        # ([], [[]]),
        (
            [1, 1, 2, 2],
            [
                [],
                [1],
                [1, 1],
                [1, 1, 2],
                [1, 1, 2, 2],
                [1, 2],
                [1, 2, 2],
                [2],
                [2, 2],
            ],
        ),
        # Add more test cases as needed
    ],
)
def test_subsetsWithDup(nums: list[int], expected_result: list[list[int]]):
    solution = Solution()
    result = solution.subsetsWithDup(nums)
    assert result == expected_result
