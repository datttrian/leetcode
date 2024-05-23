def getSubsets(nums: list[int]) -> list[list[int]]:
    res: list[list[int]] = []
    for num in nums:
        res += [curr + [num] for curr in res]
        res.append([num])
    return res


def isBeautiful(nums: list[int], k: int) -> bool:
    nums_set = set(nums)
    for num in nums:
        if (num + k) in nums_set or (num - k) in nums_set:
            return False
    return True


nums = [2, 4, 6]
subsets = getSubsets(nums)
print(subsets)

result = [subset for subset in subsets if isBeautiful(subset, 2)]
print(len(result))
