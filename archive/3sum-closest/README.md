# 3Sum Closest


Given an integer array `nums` of length `n` and an integer `target`,
find three integers in `nums` such that the sum is closest to `target`.

Return *the sum of the three integers*.

You may assume that each input would have exactly one solution.

 

**Example 1:**

    Input: nums = [-1,2,1,-4], target = 1
        Output: 2
        Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
        

**Example 2:**

    Input: nums = [0,0,0], target = 1
        Output: 0
        Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
        

 

**Constraints:**

- `3 <= nums.length <= 500`
- `-1000 <= nums[i] <= 1000`
- `-10`^(`4`)` <= target <= 10`^(`4`)


# Intuition
The problem is to find the closest possible sum of a triplet in the given sorted integer array 'nums' to the specified 'target' value. The two-pointer approach is used to efficiently explore triplet combinations and narrow down the closest sum.

# Approach
1. The input array 'nums' is sorted to simplify the two-pointer approach.
2. The algorithm initializes a variable, `closest_sum`, to store the closest sum found so far. It is initially set to positive infinity.
3. The algorithm iterates through the array up to the third-to-last element, fixing one element at a time.
4. Two pointers, `left` and `right`, are initialized within the remaining elements.
5. The algorithm continues searching for a triplet sum while the `left` pointer is less than the `right` pointer.
6. The current sum of the triplet, `current_sum`, is calculated.
7. The `closest_sum` is updated if the current triplet sum is closer to the target than the previously recorded closest sum.
8. The pointers are adjusted based on the comparison of the `current_sum` with the target.
9. If the `current_sum` is equal to the target, the algorithm returns it immediately as it is the closest possible sum.
10. The closest_sum found after iterating through all possible triplets is returned.

# Complexity
- Time complexity: O(n^2), where 'n' is the length of the input array 'nums'. The algorithm iterates through the array and uses a two-pointer approach.
- Space complexity: O(1), as the method only uses a constant amount of extra space.

# Code
```python
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> float:
        # Sort the input array to simplify the two-pointer approach
        nums.sort()

        # Initialize a variable to store the closest sum found so far
        closest_sum = float('inf')

        # Iterate through the array up to the third-to-last element
        for i in range(len(nums) - 2):
            # Initialize two pointers, left and right, within the remaining elements
            left, right = i + 1, len(nums) - 1

            # Continue searching for a triplet sum while the left pointer is less than the right pointer
            while left < right:
                # Calculate the current sum of the triplet
                current_sum = nums[i] + nums[left] + nums[right]

                # Update the closest_sum if the current triplet sum is closer to the target
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                # Adjust pointers based on the comparison of the current_sum with the target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # If the current_sum is equal to the target, return it immediately as it is the closest possible
                    return closest_sum

        # Return the closest_sum found after iterating through all possible triplets
        return closest_sum
```

The code is well-documented, and the two-pointer approach efficiently finds the closest possible sum of a triplet to the target.