from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0

        for i, num in enumerate(nums):
            if num != val:
                nums[i] = num
                i += 1

        return i
