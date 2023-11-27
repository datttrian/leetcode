# Longest Substring Without Repeating Characters


Given a string `s`, find the length of the **longest** **substring** without repeating characters.

 

**Example 1:**

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

**Example 2:**

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

**Example 3:**

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

**Constraints:**

- `0 <= s.length <= 5 * 10`^(`4`)
- `s` consists of English letters, digits, symbols and spaces.


# Intuition
The problem is to find the length of the longest substring without repeating characters in a given string. The sliding window approach is employed here. A window is maintained, and as it slides through the string, a dictionary is used to keep track of the most recent index of each character encountered. When a repeating character is found, the left boundary of the window is moved to one past the last occurrence of that character.

# Approach
1. Initialize an empty dictionary (`char_index_map`) to store the most recent index of each character.
2. Initialize the left boundary of the current window (`left`) to 0.
3. Initialize the length of the longest substring found (`max_length`) to 0.
4. Enumerate over each character in the string (`s`).
   - Check if the character has been seen and is within the current window.
     - If yes, move the left boundary to one past the last occurrence of the current character.
   - Update the character's latest index in the dictionary.
   - Update the maximum length if the current window size is larger.
5. Return the length of the longest substring found (`max_length`).

# Complexity
- Time complexity: O(n), where n is the length of the string. The function iterates through the string once with constant-time operations at each step.
- Space complexity: O(min(m, n)), where m is the size of the character set, and n is the length of the string. In the worst case, the whole string might be stored in the dictionary, but typically the size is limited by the character set.

# Code
```python
from typing import Dict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map: Dict[str, int] = {}
        left: int = 0
        max_length: int = 0

        for right, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1

            char_index_map[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length
```