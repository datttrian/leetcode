import pytest
from subsets import Solution


@pytest.mark.parametrize(
    ["nums", "expected"],
    [
        [[1], [[], [1]]],
        [[1, 2], [[], [1], [2], [1, 2]]],
        [[1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]],
        [
            [1, 2, 3, 4],
            [
                [],
                [1],
                [2],
                [1, 2],
                [3],
                [1, 3],
                [2, 3],
                [1, 2, 3],
                [4],
                [1, 4],
                [2, 4],
                [1, 2, 4],
                [3, 4],
                [1, 3, 4],
                [2, 3, 4],
                [1, 2, 3, 4],
            ],
        ],
    ],
)
def test_subsets(nums: list[int], expected: list[list[int]]) -> None:
    solution = Solution()
    result = solution.subsets(nums)

    result_sorted = sorted([sorted(subset) for subset in result])
    expected_sorted = sorted([sorted(subset) for subset in expected])

    assert result_sorted == expected_sorted
