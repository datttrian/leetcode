from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int):
        """
        Find and return the indices of two numbers in the 'nums' list that add up to the 'target'.

        Args:
            nums (List[int]): The list of integers to search for a pair.
            target (int): The target sum to find.

        Returns:
            List[int]: A list containing the indices of the two numbers that add up to the target.
                       If no such pair is found, an empty list is returned.
        """
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []
