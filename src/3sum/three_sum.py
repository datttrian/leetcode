from typing import List, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[Tuple[int, int, int]]:
        """
        Find all unique triplets in the given list of integers that sum up to
        zero.

        This method employs a two-pointer approach on a sorted list of
        integers to efficiently locate unique triplets (a, b, c) where a + b +
        c = 0. The algorithm avoids duplicate triplets and
        ensures uniqueness within each triplet.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            List[Tuple[int, int, int]]: A list of tuples representing unique
            triplets, where each triplet (a, b, c) satisfies the condition a +
            b + c = 0.

        Note:
            The input list is sorted in non-decreasing order to facilitate the
            two-pointer approach. The algorithm avoids duplicate triplets and
            elements within a triplet.

        Example:
            >>> solution = Solution()
            >>> nums = [-1, 0, 1, 2, -1, -4]
            >>> solution.threeSum(nums)
            [(-1, -1, 2), (-1, 0, 1)]

        """
        # Implementation of the 3Sum problem using a two-pointer approach
        nums.sort()
        result: List[Tuple[int, int, int]] = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result
