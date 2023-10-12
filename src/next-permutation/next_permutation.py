from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Pivot is the element just before the non-increasing
        # (weakly decreasing) suffix
        pivot = self.indexOfLastPeak(nums) - 1
        # Partition nums into [prefix pivot suffix]
        if pivot != -1:
            nextPrefix = self.lastIndexOfGreater(nums, nums[pivot])
            # Next prefix must exist because pivot < suffix[0], otherwise pivot
            # would be part of suffix
            self.swap(nums, pivot, nextPrefix)
        self.reverseSuffix(nums, pivot + 1)

    def indexOfLastPeak(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                return i
        return 0

    def lastIndexOfGreater(self, nums: List[int], threshold: int) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if threshold < nums[i]:
                return i
        return -1

    def reverseSuffix(self, nums: List[int], start: int) -> None:
        end = len(nums) - 1
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1

    def swap(self, nums: List[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]
