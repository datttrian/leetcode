from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Return True if you can reach the last index, False otherwise.

        Parameters:
        - nums (List[int]): The input integer array representing maximum jump
        lengths.

        Returns:
        - bool: True if you can reach the last index, False otherwise.
        """
        max_reach = 0
        n = len(nums)

        for i in range(n):
            if i > max_reach:
                return False  # If the current index is not reachable
            max_reach = max(max_reach, i + nums[i])

            if max_reach >= n - 1:
                return True  # If the last index is reachable

        return False
