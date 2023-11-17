# Longest Palindromic Substring


Given a string `s`, return *the longest* palindromic substring in `s`.

 

**Example 1:**

    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

**Example 2:**

    Input: s = "cbbd"
    Output: "bb"

 

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.


# Intuition
The problem is to find the longest palindromic substring in the given string. The solution employs the Expand Around Center technique. It considers each index in the string as the middle of a potential palindrome and expands outwards to check for palindrome conditions. The algorithm expands around each character (for odd-length palindromes) and each pair of consecutive characters (for even-length palindromes), updating the longest palindrome found.

# Approach
1. Initialize an empty string (`res`) to hold the longest palindrome found.
2. Initialize the length of the longest palindrome found (`resLen`) to 0.
3. For each character in the string (`s`), attempt to find the longest palindrome with the character as the center for odd-length palindromes:
   - Initialize two pointers (`l` and `r`) at the current index.
   - While the pointers are within the bounds of the string and the characters at positions `l` and `r` are equal, expand the considered range to the left and right.
   - If the currently considered substring is a palindrome and its length is greater than the length of the previously recorded longest palindrome, update `res` and `resLen`.
4. After checking for odd-length palindromes with center `i`, check for even-length palindromes by considering the center to be between `i` and `i+1`:
   - Initialize `l` at the current index and `r` at the next index.
   - While the pointers are within the bounds of the string and the characters at positions `l` and `r` are equal, expand the considered range to the left and right.
   - If the currently considered substring is a palindrome and its length is greater than the length of the previously recorded longest palindrome, update `res` and `resLen`.
5. After checking all characters and all possible centers for palindromes, return the longest palindrome found in the string.

# Complexity
- Time complexity: O(n^2), where n is the length of the input string. This time complexity arises from the fact that for each of the n characters, the expansion could potentially go through the rest of the string.
- Space complexity: O(1), as the space used does not depend on the size of the input string, and only a constant amount of extra space is used.

# Code
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''  # String to hold the longest palindrome found
        resLen = 0  # The length of the longest palindrome found

        for i in range(len(s)):
            # Odd-length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # Even-length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res
```