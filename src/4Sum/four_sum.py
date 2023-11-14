from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Find all unique quadruplets in the given list of integers that sum up
        to the target.

        The algorithm employs a two-pointers approach along with sorting to
        efficiently explore and eliminate duplicate combinations. It iterates
        through the sorted array, selecting pairs of elements and using two
        pointers to find the remaining two elements that sum up to the target.
        Duplicate combinations are skipped to ensure the uniqueness of the
        results.

        Parameters:
        - nums (List[int]): The input list of integers.
        - target (int): The target sum that the quadruplets should achieve.

        Returns:
        List[List[int]]: A list of lists, each representing a unique
        quadruplet that sums up to the target.

        Raises:
        (No specific exceptions are raised)

        Complexity:
        - Time: O(n^3), where n is the length of the input list `nums`.
        The algorithm uses nested loops, and each iteration involves a
        two-pointers traversal.

        - Space: O(1), as the algorithm uses a constant amount of extra space
        for variables and the result list.
        """
        # Sort the input array to simplify the solution
        nums.sort()

        # Initialize an empty list to store the resulting quadruplets
        result: List[List[int]] = []

        # Get the length of the input array for iteration
        n = len(nums)

        # Iterate through the array, considering the first element of the
        # quadruplet
        for i in range(n - 3):
            # Skip duplicate values to avoid duplicate quadruplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Iterate through the array, considering the second element of the
            # quadruplet
            for j in range(i + 1, n - 2):
                # Skip duplicate values to avoid duplicate quadruplets
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Initialize pointers for the remaining two elements of the
                # quadruplet
                left, right = j + 1, n - 1

                # Use two pointers approach to find the remaining elements
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    # Check if the current combination equals the target
                    if curr_sum == target:
                        # Append the quadruplet to the result list
                        result.append(
                            [nums[i], nums[j], nums[left], nums[right]],
                        )

                        # Skip duplicate values for the remaining two elements
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # Move the pointers to explore new combinations
                        left += 1
                        right -= 1
                    elif curr_sum < target:
                        # Adjust the pointers based on the comparison with the
                        # target
                        left += 1
                    else:
                        right -= 1

        # Return the final list of unique quadruplets that sum up to the target
        return result
