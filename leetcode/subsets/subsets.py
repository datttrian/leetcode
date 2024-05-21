class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = [[]]
        for num in nums:
            res += [curr + [num] for curr in res]
        return res
