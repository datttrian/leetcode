import pytest
from plus_one import Solution


@pytest.mark.parametrize(
    ["digits", "expected"],
    [
        [[1, 9], [2, 0]],  # Basic case with a carry.
        [[2], [3]],  # Basic case without a carry.
        [
            [9, 9, 9],
            [1, 0, 0, 0],
        ],  # Case with carry propagating through all digits.
        [[1, 2, 3], [1, 2, 4]],  # Case without carry.
        [[0], [1]],  # Minimal input case.
        [[8, 9, 9], [9, 0, 0]],  # Case with a carry at the beginning.
        [[0, 0, 0], [0, 0, 1]],  # Case with carry creating a new digit.
    ],
)
def test_plus_one(digits: list[int], expected: list[int]) -> None:
    solution = Solution()
    result = solution.plusOne(digits)
    assert result == expected
