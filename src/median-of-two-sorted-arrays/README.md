# Median of Two Sorted Arrays



Given two sorted arrays `nums1` and `nums2` of size `m` and `n`
respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

 

**Example 1:**

    Input: nums1 = [1,3], nums2 = [2]
        Output: 2.00000
        Explanation: merged array = [1,2,3] and median is 2.
        

**Example 2:**

    Input: nums1 = [1,2], nums2 = [3,4]
        Output: 2.50000
        Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
        

 

**Constraints:**

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10`^(`6`)` <= nums1[i], nums2[i] <= 10`^(`6`)


# Intuition
The problem involves finding the median of two sorted arrays. The approach used here is a binary search algorithm to find the correct partition between the arrays that would form a merged sorted array. The goal is to ensure that elements on the left side of the partition are smaller than or equal to elements on the right side. The median can then be calculated from the elements around the partition.

# Approach
1. Assign `nums1` and `nums2` to `A` and `B` such that `len(A) <= len(B)`.
2. Calculate the total length of both arrays (`total_length`) and the middle index (`half_point`).
3. Initialize the binary search on the smaller array `A` with `left_index` and `right_index`.
4. Perform a binary search to find the correct partition:
   - Find the index `i` in array `A` such that it is close to the median.
   - Find the corresponding index `j` in array `B` using `half_point`.
   - Determine the edge values around the partition to compare (use ±infinity as defaults for out-of-bound indices).
   - Check if we have found a valid partition:
      - If `Aleft <= Bright` and `Bleft <= Aright`, the partition is valid.
      - For odd total length, return the minimum of `Aright` and `Bright`.
      - For even total length, return the average of the maximum of `Aleft` and `Bleft` and the minimum of `Aright` and `Bright`.
   - If elements on the left side of `A` are greater, move the partition to the left.
   - If elements on the left side of `B` are greater, move the partition to the right.

# Complexity
- Time complexity: O(log(min(m, n))), where m and n are the lengths of the input arrays. The binary search is performed on the smaller array.
- Space complexity: O(1), as the solution uses constant extra space.

# Code
```python
from typing import List

class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int],
    ) -> float:
        A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        total_length = len(A) + len(B)
        half_point = total_length // 2
        left_index, right_index = 0, len(A) - 1

        while True:
            i = (left_index + right_index) // 2
            j = half_point - i - 2

            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i + 1] if (i + 1) < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j + 1] if (j + 1) < len(B) else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:
                if total_length % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                right_index = i - 1
            else:
                left_index = i + 1
```