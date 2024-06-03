# LeetCode

## 217. Contains Duplicate

Given an integer array `nums`, return `true` if any value appears **at
least twice** in the array, and return `false` if every element is
distinct.

**Example 1:**

    Input: nums = [1,2,3,1]
    Output: true

**Example 2:**

    Input: nums = [1,2,3,4]
    Output: false

**Example 3:**

    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

**Constraints:**

- `1 <= nums.length <= 10`<sup>`5`</sup>
- `-10`<sup>`9`</sup>`<= nums[i] <= 10`<sup>`9`</sup>

### Brute Force - O(n^2), O(1)


```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False


solution = Solution()
print(solution.containsDuplicate(nums=[1, 2, 3, 1]))
print(solution.containsDuplicate(nums=[1, 2, 3, 4]))
print(solution.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
```

    True
    False
    True


### Sorting - O(n log n), O(1)


```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


solution = Solution()
print(solution.containsDuplicate(nums=[1, 2, 3, 1]))
print(solution.containsDuplicate(nums=[1, 2, 3, 4]))
print(solution.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
```

    True
    False
    True


### Arrays & Hashing


```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_unique: set[int] = set()
        for num in nums:
            if num in nums_unique:
                return True
            nums_unique.add(num)
        return False


solution = Solution()
print(solution.containsDuplicate(nums=[1, 2, 3, 1]))
print(solution.containsDuplicate(nums=[1, 2, 3, 4]))
print(solution.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
```

    True
    False
    True

