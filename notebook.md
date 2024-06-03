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


### Arrays & Hashing - O(n), O(n)


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


## 242. Valid Anagram

Given two strings `s` and `t`, return `true` *if* `t` *is an anagram of*
`s`*, and* `false` *otherwise*.

An **Anagram** is a word or phrase formed by rearranging the letters of
a different word or phrase, typically using all the original letters
exactly once.

**Example 1:**

    Input: s = "anagram", t = "nagaram"
    Output: true

**Example 2:**

    Input: s = "rat", t = "car"
    Output: false

**Constraints:**

- `1 <= s.length, t.length <= 5 * 10`<sup>`4`</sup>
- `s` and `t` consist of lowercase English letters.

**Follow up:** What if the inputs contain Unicode characters? How would
you adapt your solution to such a case?

### Brute Force - O(n^2), O(1)


```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for char in s:
            is_found = False
            for i in range(len(t)):
                if t[i] == char:
                    t = t[:i] + t[i + 1 :]
                    is_found = True
                    break

            if not is_found:
                return False

        return True


solution = Solution()
print(solution.isAnagram(s="anagram", t="nagaram"))
print(solution.isAnagram(s="rat", t="car"))
```

    True
    False
