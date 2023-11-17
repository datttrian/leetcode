from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Summary:
        Find two indices in an integer array whose values sum up to a given
        target number.

        Intuition:
        The problem requires finding two indices in an integer array whose
        values sum up to a given target number. One intuitive approach is to
        iterate through the array and, for each element, check if there is
        another element in the array whose sum with the current element equals
        the target. To improve efficiency, we can use a dictionary to store
        the numbers and their corresponding indices as we iterate through the
        array.

        Approach:
        - Create a dictionary (`num_dict`) to store numbers and their indices.
        - Iterate over the list of numbers.
        - For each number, calculate the complement by subtracting it from the
        target.
        - If the complement is in the dictionary, return the indices of the
        two numbers.
        - If no solution is found, return an empty list.

        Complexity:
        - Time: O(n), where n is the number of elements in `nums`. The
        function iterates through the list only once.
        - Space: O(n), for the dictionary used to store the number indices.

        Raises:
        - This function assumes that there is exactly one solution, and it
        does not handle the case where no solution exists.
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
