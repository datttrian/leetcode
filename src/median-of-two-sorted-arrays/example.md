The `findMedianSortedArrays` function in the `Solution` class calculates the median of two sorted arrays, efficiently handling the cases where the arrays are of different lengths and the median might not be a direct member of either array. This implementation uses binary search, which is particularly efficient with time complexity `O(log(min(m, n)))`, where `m` and `n` are the lengths of the two input arrays. Here is a step-by-step explanation using two arrays as examples:

Assume `nums1 = [1, 3]` and `nums2 = [2]`.

1. **Initialization**:
   - Check which array is smaller; in this case, `nums1` is smaller (`m <= n`), so `A = nums1` and `B = nums2`.
   - Calculate the total length `total_length = 3` and `half_point = 1`.

2. **Binary Search**:
   - Start with a binary search on the smaller array `A`.
   - Initialize the binary search indices `left_index = 0` and `right_index = len(A) - 1 = 1`.

3. **First Iteration**:
   - Calculate `i = (0 + 1) // 2 = 0` and `j = 1 - 0 - 2 = -1`.
   - Determine the edge values around the partition:
     - `Aleft = A[0] = 1`
     - `Aright = A[1] = 3`
     - `Bleft = float('-infinity')` (because `j = -1` is out of bounds)
     - `Bright = B[0] = 2`
   - The conditions for a correct partition are met because `Aleft <= Bright` and `Bleft <= Aright`.

4. **Median Calculation**:
   - Since `total_length % 2 != 0`, the median is the first middle element from the right, which is `min(Aright, Bright) = min(3, 2) = 2`.

So, the median of `[1, 3]` and `[2]` is `2`.

This process involves continually narrowing the search space by shifting the partition in the smaller array (`A`) until the partition satisfies the conditions where every element on the left side of the partition is less than or equal to every element on the right side of the partition. The median is then found based on whether the total number of elements is odd or even. If it's odd, the median is the first middle element on the right side of the partition. If it's even, it's the average of the two middle elements, one from each side of the partition.


Given the two sorted arrays:

```python
nums1 = [1, 4, 5, 7, 8, 9]
nums2 = [2, 3, 4, 6, 7, 9, 13, 14]
```

We want to find the median of the combined array. Here's a step-by-step explanation of how the `findMedianSortedArrays` method would work with these arrays:

1. **Initialization**:
    - Since `len(nums1) <= len(nums2)`, we assign `A = nums1` and `B = nums2`.
    - The total length of both arrays is `6 + 8 = 14`. The halfway point is `14 // 2 = 7`.

2. **Binary Search**:
    - We set `left_index = 0` and `right_index = len(A) - 1 = 5`.

3. **First Iteration**:
    - We calculate the partition index for A using `i = (left_index + right_index) // 2`. Initially, this is `(0 + 5) // 2 = 2`.
    - For B, we calculate `j = half_point - i - 2`. Initially, this is `7 - 2 - 2 = 3`.

4. **Check Partition**:
    - We examine the elements around the partition:
        - `Aleft = A[i] = 5`
        - `Aright = A[i + 1] = 7`
        - `Bleft = B[j] = 6`
        - `Bright = B[j + 1] = 7`
    - We check if `Aleft <= Bright` and `Bleft <= Aright`. In this case, `5 <= 7` and `6 <= 7`, so the partition is correct.

5. **Find Median**:
    - Since the total length of the combined array is even (14), the median is the average of the two middle numbers.
    - We find the two middle numbers around the partition, which are `B[j]` and `A[i + 1]` (or `Bleft` and `Aright`), both of which are `7` in this case.
    - The median is `(max(Aleft, Bleft) + min(Aright, Bright)) / 2`. Therefore, it's `(max(5, 6) + min(7, 7)) / 2 = (6 + 7) / 2 = 13 / 2 = 6.5`.

Hence, the median of the two arrays combined is `6.5`.
