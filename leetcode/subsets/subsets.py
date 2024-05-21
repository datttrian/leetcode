def subsets(nums: list[int]) -> list[list[int]]:
    res: list[list[int]] = [[]]
    for num in nums:
        res += [curr + [num] for curr in res]
    return res


# Example usage:
nums1: list[int] = []
print(subsets(nums1))

nums2 = [-5]
print(subsets(nums2))

nums3 = [-1, 0, 1]
print(subsets(nums3))

nums4 = [-1, 1]
print(subsets(nums4))

nums5 = [-10, 0, 10]
print(subsets(nums5))

nums6 = [1, 2, 3, 4]
print(subsets(nums4))
