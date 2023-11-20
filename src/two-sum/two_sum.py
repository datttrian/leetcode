from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find indices of the two numbers in the given list that add up to the
        target.

        Parameters:
        - nums (List[int]): A list of integers.
          The input list in which the two numbers are searched.
        - target (int): Target sum that the pair of numbers should achieve.

        Returns:
        - List[int]: A list containing two indices (integers) of the numbers
          in the input list that add up to the target. If no such pair is
          found,
          an empty list is returned.

        Raises:
        - None: No explicit exceptions are raised in this implementation.
          The problem statement guarantees at least one solution, so there
          will always be a pair of numbers adding up to the target.
        """
        # Create a dictionary to store the numbers and their indices
        num_dict: Dict[int, int] = {}

        # Iterate over the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num

            # If the complement is in the dictionary, we have found a pair
            if complement in num_dict:
                # Return the indices of the two numbers adding up to the target
                return [num_dict[complement], i]

            # Store the number and its index in the dictionary
            num_dict[num] = i

        # If no solution is found, this line will not be executed because the
        # problem statement guarantees at least one solution
        return []
