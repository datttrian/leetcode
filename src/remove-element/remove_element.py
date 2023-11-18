from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize the pointer
        i = 0

        # Iterate through the array using enumerate
        for i, num in enumerate(nums):
            # If the current element is not equal to val
            if num != val:
                # Swap the current element with the element at the i-th
                # position
                nums[i] = num
                i += 1

        return i
