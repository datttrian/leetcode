import pytest
from relative_ranks import Solution


@pytest.mark.parametrize(
    "scores, expected",
    [
        (
            [5, 4, 3, 2, 1],
            ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"],
        ),
        (
            [1, 2, 3, 4, 5],
            ["5", "4", "Bronze Medal", "Silver Medal", "Gold Medal"],
        ),
    ],
)
def test_findRelativeRanks(scores: list[int], expected: list[str]) -> None:
    solution = Solution()
    assert solution.findRelativeRanks(scores) == expected
