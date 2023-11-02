from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numsset = nums
        numsset = set(numsset)
        numsset = list(numsset)
        numsset.sort()
        # print(numsset)
        # print(nums)
        nums[: len(numsset) + 1] = numsset[:]
        nums[:] = sorted(set(nums))
        return len(nums)
