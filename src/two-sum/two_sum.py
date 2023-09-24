"""
Module docstring: This module contains a solution to the two-sum problem.
"""

from typing import List


class Solution:
    """
    Class docstring: This class provides a solution to the two-sum problem.
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []
