from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the numbers and their indices
        num_dict: Dict[int, int] = {}
        # Iterate over the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            # If the complement is in the dictionary, we have found a solution
            if complement in num_dict:
                return [num_dict[complement], i]
            # Otherwise, add the number to the dictionary
            num_dict[num] = i
        # If no solution is found, this line will never be reached
        return []
