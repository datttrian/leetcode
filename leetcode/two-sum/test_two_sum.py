from two_sum import Solution


def test_two_sum() -> None:
    solution = Solution()

    # Test case 1
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    result = solution.twoSum(nums, target)
    assert result == expected, f"Test case 1 failed: {result}"

    # Test case 2
    nums = [3, 2, 4]
    target = 6
    expected = [1, 2]
    result = solution.twoSum(nums, target)
    assert result == expected, f"Test case 2 failed: {result}"

    # Test case 3
    nums = [3, 3]
    target = 6
    expected = [0, 1]
    result = solution.twoSum(nums, target)
    assert result == expected, f"Test case 3 failed: {result}"


if __name__ == "__main__":
    test_two_sum()
