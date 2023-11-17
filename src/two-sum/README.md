# Two Sum


Given an array of integers `nums` and an integer `target`, return
*indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly* one solution**,
and you may not use the *same* element twice.

You can return the answer in any order.

 

**Example 1:**

    Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        

**Example 2:**

    Input: nums = [3,2,4], target = 6
        Output: [1,2]
        

**Example 3:**

    Input: nums = [3,3], target = 6
        Output: [0,1]
        

 

**Constraints:**

- `2 <= nums.length <= 10`^(`4`)
- `-10`^(`9`)` <= nums[i] <= 10`^(`9`)
- `-10`^(`9`)` <= target <= 10`^(`9`)
- **Only one valid answer exists.**

 

**Follow-up: **Can you come up with an algorithm that is less than
`O(n`^(`2`)`)`  time complexity?

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
```