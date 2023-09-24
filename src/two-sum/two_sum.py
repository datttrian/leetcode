from typing import List


class Solution:
    # Define a method 'twoSum' that takes a list of integers 'nums' and an integer 'target' as input.
    # The method returns a list of integers representing the indices of the two numbers in 'nums'
    # that add up to the 'target', or an empty list if no such pair is found.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary 'numMap' to store numbers from 'nums' as keys and their
        # corresponding indices as values.
        numMap = {}
        
        # Get the length of the 'nums' list.
        n = len(nums)

        # Iterate through the elements of the 'nums' list using their indices.
        for i in range(n):
            # Calculate the complement, which is the difference between the 'target' and the current
            # element in 'nums'. This is the value we need to find in 'numMap' to form the target sum.
            complement = target - nums[i]
            
            # Check if the 'complement' is already in 'numMap'.
            if complement in numMap:
                # If it is, return a list containing the index of the 'complement' and the current index 'i'.
                return [numMap[complement], i]
            
            # If the 'complement' is not in 'numMap', store the current element 'nums[i]' as a key
            # in 'numMap' with its value set to 'i'. This will help us look up the complement in
            # future iterations.
            numMap[nums[i]] = i

        # If no valid pair is found in the 'nums' list that adds up to the 'target', return an empty list.
        return []
