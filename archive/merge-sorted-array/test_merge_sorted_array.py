import pytest
from merge_sorted_array import Solution


@pytest.mark.parametrize(
    ('nums1', 'm', 'nums2', 'n', 'expected_result'),
    [
        # Test case with equal-length sorted arrays
        # ([1, 2, 3], 3, [4, 5, 6], 3, [1, 2, 3, 4, 5, 6]),
        # Test case with nums1 longer than nums2
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        # Test case with nums2 longer than nums1
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
        # Test case with empty nums1
        # ([], 0, [1, 2, 3], 3, [1, 2, 3]),
        # Test case with empty nums2
        ([1, 2, 3], 3, [], 0, [1, 2, 3]),
        # Test case with empty nums1 and nums2
        ([], 0, [], 0, []),
        # Test case with equal-length reverse sorted arrays
        # ([3, 2, 1], 3, [6, 5, 4], 3, [1, 2, 3, 4, 5, 6]),
    ],
)
def test_merge(
    nums1: list[int],
    m: int,
    nums2: list[int],
    n: int,
    expected_result: list[int],
):
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    assert nums1 == expected_result
