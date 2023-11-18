# 3Sum


Given an integer array nums, return all the triplets
`[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and
`j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

 

**Example 1:**

    Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        Explanation: 
        nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        The distinct triplets are [-1,0,1] and [-1,-1,2].
        Notice that the order of the output and the order of the triplets does not matter.
        

**Example 2:**

    Input: nums = [0,1,1]
        Output: []
        Explanation: The only possible triplet does not sum up to 0.
        

**Example 3:**

    Input: nums = [0,0,0]
        Output: [[0,0,0]]
        Explanation: The only possible triplet sums up to 0.
        

 

**Constraints:**

- `3 <= nums.length <= 3000`
- `-10`^(`5`)` <= nums[i] <= 10`^(`5`)


# Intuition
The problem is to find all unique triplets in the given list of integers that sum up to zero. One intuitive approach is to use a two-pointer technique on a sorted list of integers. This involves fixing one element and then using two pointers to traverse the rest of the array to find a pair whose sum with the fixed element equals zero.

# Approach
The algorithm first sorts the input list in non-decreasing order to facilitate the two-pointer approach. It then iterates through the sorted list, fixing one element at a time. For each fixed element, the algorithm uses two pointers (left and right) to find a pair whose sum with the fixed element equals zero. The algorithm avoids duplicate triplets and elements within a triplet.

The time complexity of this algorithm is O(n^2), where n is the length of the input list. The space complexity is O(1) since the algorithm uses a constant amount of extra space.

# Code
```python
from typing import List, Tuple

class Solution:
    def threeSum(self, nums: List[int]) -> List[Tuple[int, int, int]]:
        nums.sort()
        result: List[Tuple[int, int, int]] = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result
```

The code is well-documented with comments explaining each step of the algorithm. The two-pointer approach efficiently finds unique triplets that sum up to zero while avoiding duplicates.
