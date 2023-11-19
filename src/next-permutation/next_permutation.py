from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        # Find the first index i from the right such that nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # If such index is found, find the smallest element to the right of i
        # that is greater than nums[i]
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the subarray to the right of i
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
