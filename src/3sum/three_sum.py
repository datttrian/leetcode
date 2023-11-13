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
        # Sort the input list to facilitate the two-pointer approach
        nums.sort()

        # Initialize the result list to store unique triplets
        result: List[Tuple[int, int, int]] = []

        # Iterate through the sorted list, considering each element as the
        # potential first element of the triplet
        for i in range(len(nums) - 2):
            # Avoid duplicates for the first element of the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize left and right pointers for the remaining elements in
            # the list
            left, right = i + 1, len(nums) - 1

            # Use a two-pointer approach to find the other two elements that
            # sum to zero
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # Adjust pointers based on the sum
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # Found a triplet, add it to the result list
                    result.append((nums[i], nums[left], nums[right]))

                    # Skip duplicates for the second and third elements of the
                    # triplet
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        # Return the list of unique triplets that sum to zero
        return result
