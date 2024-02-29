# Longest Common Prefix

Write a function to find the longest common prefix string amongst an
array of strings.

If there is no common prefix, return an empty string `""`.

 

**Example 1:**

    Input: strs = ["flower","flow","flight"]
        Output: "fl"
        

**Example 2:**

    Input: strs = ["dog","racecar","car"]
        Output: ""
        Explanation: There is no common prefix among the input strings.
        

 

**Constraints:**

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters.


# Intuition
The goal is to find the longest common prefix among a list of strings. The solution sorts the list of strings to bring similar prefixes together and then compares the characters at each position in the first and last strings after sorting.

# Approach
1. Check if the input list (`strs`) is empty. If it is, return an empty string.
2. Sort the list of strings to bring similar prefixes together.
3. Take the first and last strings after sorting (`first_str` and `last_str`).
4. Initialize an empty list (`common_prefix`) to store the common prefix characters.
5. Use the `enumerate` function to iterate through characters with their indices in the `first_str`.
6. For each character at index `i`, check if the current index is within the length of `last_str` and if the character matches between `first_str` and `last_str`.
7. If there is a match, append the character to the `common_prefix` list.
8. If there is a mismatch, break the loop, indicating the end of the common prefix.
9. Join the list of common prefix characters into a single string and return the result.

# Time Complexity
The time complexity is O(n * m * log(n)), where:
- n is the number of strings in the input list (`strs`).
- m is the average length of the strings.
The sorting step dominates the time complexity.

# Space Complexity
The space complexity is O(m), where m is the length of the common prefix. The space complexity is determined by the list storing the common prefix characters.

# Code
```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Check if the input list is empty
        if not strs:
            return ''

        # Sort the list of strings to bring similar prefixes together
        strs.sort()

        # Take the first and last strings after sorting
        first_str = strs[0]
        last_str = strs[-1]

        # Initialize an empty list to store the common prefix characters
        common_prefix: List[str] = []

        # Use enumerate to iterate through characters with their indices
        for i, char in enumerate(first_str):
            # Check if the current index is within the length of the last
            # string and if the character matches between the first and last
            # strings
            if i < len(last_str) and char == last_str[i]:
                common_prefix.append(char)
            else:
                # Break the loop if there is a mismatch, indicating the end of
                # the common prefix
                break

        # Join the list of common prefix characters into a single string and
        # return
        return ''.join(common_prefix)
```