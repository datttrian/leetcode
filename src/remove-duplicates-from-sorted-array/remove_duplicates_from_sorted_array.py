from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from a sorted list in-place and returns the new
        length.

        Summary:
        Given a sorted list, this function modifies the list in-place to
        remove duplicate elements, and returns the length of the modified list
        without duplicates.

        Description:
        The function iterates through the sorted list and maintains a pointer
        'k' representing the index where the next unique element should be
        placed. If the current element is different from the previous one, it
        is placed at index 'k', and 'k' is incremented. At the end of the
        iteration, the modified list is truncated to the length 'k', and 'k'
        is returned.

        Algorithm:
        1. Initialize a pointer 'k' to 1 (since the first element is always
        unique).
        2. Iterate through the list starting from index 1.
        3. If the current element is different from the previous one, place it
        at index 'k' and increment 'k'.
        4. After the iteration, truncate the list to the length 'k'.
        5. Return the value of 'k', which represents the new length of the
        list without duplicates.

        Parameters:
        - nums (List[int]): A sorted list of integers with possible duplicate
        elements.

        Returns:
        - int: The length of the modified list without duplicates.

        Raises:
        - No explicit exceptions are raised.

        Complexity:
        - Time: O(n), where n is the length of the input list 'nums'.
        - Space: O(1), as the modification is done in-place, and the algorithm
        uses constant space.
        """
        # Check if the input list is empty
        if not nums:
            return 0

        # Initialize the pointer 'k' to 1 (the first element is always unique)
        k = 1

        # Iterate through the list starting from index 1
        for i in range(1, len(nums)):
            # If the current element is different from the previous one
            if nums[i] != nums[i - 1]:
                # Place it at index 'k' and increment 'k'
                nums[k] = nums[i]
                k += 1

        # Truncate the list to the length 'k' and return 'k'
        return k
