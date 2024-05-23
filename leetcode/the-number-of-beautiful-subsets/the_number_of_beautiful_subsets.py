def get_subsets(nums: list[int]) -> list[list[int]]:
    res: list[list[int]] = [[]]
    for num in nums:
        res += [curr + [num] for curr in res]
    return res


# Example usage:
nums = [1, 2, 3]
print(get_subsets(nums))
