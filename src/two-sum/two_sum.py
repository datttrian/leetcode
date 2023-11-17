from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two indices in an integer array whose values sum up to a given
        target number.

        The function uses a hash table to store the numbers and their
        corresponding indices. It iterates through the list of numbers only
        once, checking for each number whether there is a complement in the
        hash table (i.e., a number which, when added to the current number,
        equals the target). If such a complement is found, the function
        immediately returns a list containing the indices of the two numbers.
        If no two numbers add up to the target, the function returns an empty
        list.

        Parameters:
        - nums (List[int]): List of integers to search within.
        - target (int): The target sum to find.

        Returns:
        - List[int]: A list containing the indices of the two numbers that add
        up to the target.

        Raises:
        - This function assumes that there is exactly one solution, and it
        does not handle the case where no solution exists.

        Algorithm:
        - Create a dictionary (`num_dict`) to store the numbers and their
        indices.
        - Iterate over the list of numbers.
        - For each number, calculate the complement of the current number by
        subtracting it from the target.
        - If the complement is in the dictionary, return the indices of the
        two numbers adding up to the target.
        - If no solution is found, return an empty list.

        Complexity:
        - Time: O(n), where n is the number of elements in `nums`. The
        function iterates through the list only once.
        - Space: O(n), for the dictionary used to store the number indices.
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
