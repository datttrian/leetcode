# Container With Most Water

You are given an integer array `height` of length `n`. There are `n`
vertical lines drawn such that the two endpoints of the `i`^(`th`) line
are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that
the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

 

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

    Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
        

**Example 2:**

    Input: height = [1,1]
        Output: 1
        

 

**Constraints:**

- `n == height.length`
- `2 <= n <= 10`^(`5`)
- `0 <= height[i] <= 10`^(`4`)


# Intuition
The problem is to calculate the maximum water volume that can be trapped between the walls represented by the given array of heights. The approach uses a two-pointer approach, starting from the outermost walls and gradually moving towards each other. At each step, the potential water volume is calculated by considering the minimum height between the two walls and the distance between them. The pointers are then moved towards each other based on the comparison of wall heights. The process continues until the pointers meet.

# Approach
1. Initialize variables to keep track of the maximum water volume (`max_water`) and pointers for two walls (`left` and `right`).
2. Continue the loop until the pointers meet (`left < right`).
   - Calculate the height of the smaller wall between the two pointers (`h = min(height[left], height[right])`).
   - Calculate the width between the two walls (`w = right - left`).
   - Update the maximum water volume if the current configuration yields more water (`max_water = max(max_water, h * w)`).
   - Move the pointer pointing to the smaller wall inward, as that may lead to a larger area. If `height[left] < height[right]`, increment `left`; otherwise, decrement `right`.
3. Return the maximum water volume calculated for the given array of wall heights.

# Time Complexity
The algorithm has a time complexity of O(n), where n is the length of the input list. The two pointers move towards each other in a linear fashion, and each step involves constant-time operations.

# Space Complexity
The function has a constant space complexity as it only uses a fixed number of variables (`max_water`, `left`, and `right`).

# Code
```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_water = max(max_water, h * w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
```