import pytest
from k_th_smallest_prime_fraction import (
    Solution,
)


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 2, 3, 5], 3, [2, 5]),
        (
            [3, 5],
            1,
            [3, 5],
        ),
    ],
)
def test_kth_smallest_prime_fraction(
    arr: list[int], k: int, expected: list[int]
) -> None:
    solution = Solution()
    assert solution.kthSmallestPrimeFraction(arr, k) == expected
