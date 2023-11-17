# Intuition
The problem requires finding two indices in an integer array whose values sum up to a given target number. One intuitive approach is to iterate through the array and, for each element, check if there is another element in the array whose sum with the current element equals the target. To improve efficiency, we can use a dictionary to store the numbers and their corresponding indices as we iterate through the array.

# Approach
1. Initialize an empty dictionary (`num_dict`) to store numbers and their indices.
2. Iterate through the list of numbers (`nums`) using the `enumerate` function to keep track of the current index.
3. For each number in the list, calculate the complement (the difference between the target and the current number).
4. Check if the complement is already in the dictionary. If it is, return a list containing the indices of the two numbers that add up to the target.
5. If the complement is not in the dictionary, store the current number and its index in the dictionary.
6. If no solution is found during the iteration, return an empty list.

# Complexity
- Time complexity: O(n), where n is the number of elements in `nums`. The function iterates through the list only once.
- Space complexity: O(n), for the dictionary used to store the number indices.

# Code
```python
from typing import List, Dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict: Dict[int, int] = {}  # Dictionary to store numbers and their indices

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_dict:
                return [num_dict[complement], i]

            num_dict[num] = i

        return []
```