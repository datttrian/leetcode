from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> float:
        """
        Find the closest possible sum of a triplet in the given sorted
        integer array 'nums' to the specified 'target' value.

        Description:
        This method employs a two-pointer approach to efficiently explore
        triplet combinations. It iterates through the sorted array,
        maintaining two pointers to elements, and adjusts them based on the
        comparison of the current triplet sum with the target. The closest sum
        to the target is continuously updated during the iteration.

        Parameters:
        - nums (List[int]): A sorted list of integers.
        - target (int): The target value for the sum of triplets.

        Returns:
        float: The sum of the triplet closest to the target.

        Complexity:
        - Time: O(n^2) where 'n' is the length of the input array 'nums'.
          The algorithm iterates through the array and uses a two-pointer
          approach.
        - Space: O(1) as the method only uses a constant amount of extra space.

        Algorithm:
        1. Sort the input array to simplify the two-pointer approach.
        2. Initialize a variable to store the closest sum found so far.
        3. Iterate through the array up to the third-to-last element.
        4. Initialize two pointers, left and right, within the remaining
        elements.
        5. Continue searching for a triplet sum while the left pointer is less
        than the right pointer.
        6. Calculate the current sum of the triplet.
        7. Update the closest_sum if the current triplet sum is closer to the
        target.
        8. Adjust pointers based on the comparison of the current_sum with the
        target.
        9. If the current_sum is equal to the target, return it immediately as
        it is the closest possible.
        10. Return the closest_sum found after iterating through all possible
        triplets.
        """
        # Sort the input array to simplify the two-pointer approach
        nums.sort()

        # Initialize a variable to store the closest sum found so far
        closest_sum = float('inf')

        # Iterate through the array up to the third-to-last element
        for i in range(len(nums) - 2):
            # Initialize two pointers, left and right, within the remaining
            # elements
            left, right = i + 1, len(nums) - 1

            # Continue searching for a triplet sum while the left pointer is
            # less than the right pointer
            while left < right:
                # Calculate the current sum of the triplet
                current_sum = nums[i] + nums[left] + nums[right]

                # Update the closest_sum if the current triplet sum is closer
                # to the target
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                # Adjust pointers based on the comparison of the current_sum
                # with the target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # If the current_sum is equal to the target, return it
                    # immediately as it is the closest possible
                    return closest_sum

        # Return the closest_sum found after iterating through all possible
        # triplets
        return closest_sum
