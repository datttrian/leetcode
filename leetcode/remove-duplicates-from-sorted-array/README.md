# Remove Duplicates from Sorted Array


Given an integer array `nums` sorted in **non-decreasing order**, remove
the duplicates
[**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such
that each unique element appears only **once**. The **relative order**
of the elements should be kept the **same**. Then return *the number of
unique elements in* `nums`.

Consider the number of unique elements of `nums` to be `k`, to get
accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums`
  contain the unique elements in the order they were present in `nums`
  initially. The remaining elements of `nums` are not important as well
  as the size of `nums`.
- Return `k`.

**Custom Judge:**

The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
        int[] expectedNums = [...]; // The expected answer with correct length
        
        int k = removeDuplicates(nums); // Calls your implementation
        
        assert k == expectedNums.length;
        for (int i = 0; i < k; i++) {
            assert nums[i] == expectedNums[i];
        }
        

If all assertions pass, then your solution will be **accepted**.

 

**Example 1:**

    Input: nums = [1,1,2]
        Output: 2, nums = [1,2,_]
        Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
        It does not matter what you leave beyond the returned k (hence they are underscores).
        

**Example 2:**

    Input: nums = [0,0,1,1,1,2,2,3,3,4]
        Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
        Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
        It does not matter what you leave beyond the returned k (hence they are underscores).
        

 

**Constraints:**

- `1 <= nums.length <= 3 * 10`^(`4`)
- `-100 <= nums[i] <= 100`
- `nums` is sorted in **non-decreasing** order.


# Intuition
The intuition behind this solution is to iterate through the sorted list and maintain a pointer that represents the index where the next unique element should be placed. If the current element is different from the previous one, it is placed at the designated index, and the pointer is incremented. This approach takes advantage of the fact that the input list is already sorted.

# Approach
1. Initialize a pointer 'k' to 1 (since the first element is always unique).
2. Iterate through the list starting from index 1.
3. If the current element is different from the previous one, place it at index 'k' and increment 'k'.
4. After the iteration, truncate the list to the length 'k'.
5. Return the value of 'k', which represents the new length of the list without duplicates.

# Complexity
- Time complexity: O(n), where n is the length of the input list 'nums'. The algorithm iterates through the list once.
- Space complexity: O(1), as the modification is done in-place, and the algorithm uses constant space.

# Code
```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted list in-place and returns the new length.

        Parameters:
        - nums (List[int]): A sorted list of integers with possible duplicate elements.

        Returns:
        - int: The length of the modified list without duplicates.
        """
        # Check if the input list is empty
        if not nums:
            return 0

        # Initialize the pointer 'k' to 1 (the first element is always unique)
        k = 1

        # Iterate through the list starting from index 1
        for i in range(1, len(nums)):
            # If the current element is different from the previous one
            if nums[i] != nums[i - 1]:
                # Place it at index 'k' and increment 'k'
                nums[k] = nums[i]
                k += 1

        # Truncate the list to the length 'k' and return 'k'
        return k
```
