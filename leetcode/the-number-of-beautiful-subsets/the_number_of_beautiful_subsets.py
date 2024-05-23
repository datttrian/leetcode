class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
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

        subsets = getSubsets(nums)
        result = [subset for subset in subsets if isBeautiful(subset, k)]

        return len(result)
