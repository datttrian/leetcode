class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        def getSubsets(nums: list[int]) -> list[list[int]]:
            res: list[list[int]] = []
            for num in nums:
                res += [curr + [num] for curr in res]
                res.append([num])
            return res

        def isBeautiful(subset: list[int], k: int) -> bool:
            for i, val_i in enumerate(subset):
                for j, val_j in enumerate(subset):
                    if i != j and abs(val_i - val_j) == k:
                        return False
            return True

        subsets = getSubsets(nums)
        result = [subset for subset in subsets if isBeautiful(subset, k)]

        return len(result)
