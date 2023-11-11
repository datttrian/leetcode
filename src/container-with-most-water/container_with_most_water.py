from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Calculate the maximum water volume that can be trapped between the
        walls represented by the given array of heights.

        Parameters:
        - height (List[int]): A list of non-negative integers representing the
        heights of walls.

        Returns:
        - int: The maximum volume of water that can be trapped.

        Algorithm:
        The function uses a two-pointer approach, starting from the outermost
        walls and gradually moving towards each other. At each step, it
        calculates the potential water volume by considering the minimum
        height between the two walls and the distance between them. The
        pointers are then moved towards each other based on the comparison of
        wall heights. The process continues until the pointers meet.

        Time Complexity:
        The algorithm has a time complexity of O(n), where n is the length of
        the input list.

        Space Complexity:
        The function has a constant space complexity as it only uses a fixed
        number of variables.

        Example:
        >>> solution = Solution()
        >>> solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49
        """
        max_water = 0
        left = 0
        right = len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_water = max(max_water, h * w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
