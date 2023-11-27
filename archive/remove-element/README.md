# Remove Element


Given an integer array `nums` and an integer `val`, remove all
occurrences of `val` in `nums`
[**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm). The
order of the elements may be changed. Then return *the number of
elements in* `nums` *which are not equal to* `val`.

Consider the number of elements in `nums` which are not equal to `val`
be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums`
  contain the elements which are not equal to `val`. The remaining
  elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

**Custom Judge:**

The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
        int val = ...; // Value to remove
        int[] expectedNums = [...]; // The expected answer with correct length.
                                    // It is sorted with no values equaling val.
        
        int k = removeElement(nums, val); // Calls your implementation
        
        assert k == expectedNums.length;
        sort(nums, 0, k); // Sort the first k elements of nums
        for (int i = 0; i < actualLength; i++) {
            assert nums[i] == expectedNums[i];
        }
        

If all assertions pass, then your solution will be **accepted**.

 

**Example 1:**

    Input: nums = [3,2,2,3], val = 3
        Output: 2, nums = [2,2,_,_]
        Explanation: Your function should return k = 2, with the first two elements of nums being 2.
        It does not matter what you leave beyond the returned k (hence they are underscores).
        

**Example 2:**

    Input: nums = [0,1,2,2,3,0,4,2], val = 2
        Output: 5, nums = [0,1,4,0,3,_,_,_]
        Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
        Note that the five elements can be returned in any order.
        It does not matter what you leave beyond the returned k (hence they are underscores).
        

 

**Constraints:**

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`


# Intuition
The problem appears to involve removing all occurrences of a specific value from an array and returning the length of the modified array. The provided code seems to use a two-pointer approach to achieve this.

# Approach
The approach uses a pointer `i` to keep track of the position where non-matching elements should be placed. It iterates through the array, and whenever a non-matching element is encountered, it swaps that element with the element at position `i` and increments `i`. The final value of `i` represents the length of the modified array.

# Complexity
- Time complexity: O(n), where $$n$$ is the length of the input array `nums`. The algorithm iterates through the array once.
- Space complexity: O(1), as the algorithm uses a constant amount of extra space regardless of the input size.

The provided code is efficient and achieves the desired result with a linear time complexity.