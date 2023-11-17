# Regular Expression Matching


Given an input string `s` and a pattern `p`, implement regular
expression matching with support for `'.'` and `'*'` where:

- `'.'` Matches any single character.​​​​
- `'*'` Matches zero or more of the preceding element.

The matching should cover the **entire** input string (not partial).

 

**Example 1:**

    Input: s = "aa", p = "a"
        Output: false
        Explanation: "a" does not match the entire string "aa".
        

**Example 2:**

    Input: s = "aa", p = "a*"
        Output: true
        Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
        

**Example 3:**

    Input: s = "ab", p = ".*"
        Output: true
        Explanation: ".*" means "zero or more (*) of any character (.)".
        

 

**Constraints:**

- `1 <= s.length <= 20`
- `1 <= p.length <= 20`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `'.'`, and `'*'`.
- It is guaranteed for each appearance of the character `'*'`, there
  will be a previous valid character to match.



# Intuition
The problem is to determine if the input string 's' matches the given pattern 'p' with support for '.' (matches any single character) and '*' (matches zero or more of the preceding element). The approach uses dynamic programming to build a 2D array (`dp`) to store intermediate results of matching. The value `dp[i][j]` represents whether the first `i` characters of 's' match the first `j` characters of 'p'.

# Approach
1. Create a 2D array (`dp`) to store the intermediate results of matching. Initialize it with dimensions `(len(s) + 1) x (len(p) + 1)`.
2. Empty pattern matches an empty string (`dp[0][0] = True`).
3. Handle patterns with '*' at the beginning:
   - For each index `j` from 1 to `len(p)`, if `p[j - 1] == '*'`, consider zero occurrences of the preceding element (`dp[0][j] = dp[0][j - 2]`).
4. Use dynamic programming to fill the `dp` array:
   - For each index `i` from 1 to `len(s)` and each index `j` from 1 to `len(p)`:
     - If `p[j - 1] == s[i - 1]` or `p[j - 1] == '.'`, take the value from the diagonal (top-left) (`dp[i][j] = dp[i - 1][j - 1]`).
     - If `p[j - 1] == '*'`:
       - Consider either zero occurrences or match with the previous character:
         - `dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] if s[i - 1] == p[j - 2] or p[j - 2] == '.' else False)`.
5. The result is stored in the bottom-right cell of the `dp` array (`dp[len(s)][len(p)]`).

# Time Complexity
O(m * n), where `m` is the length of the input string 's' and `n` is the length of the pattern 'p'. The dynamic programming fills the `dp` array with a nested loop.

# Space Complexity
O(m * n), as the function uses a 2D array (`dp`) for dynamic programming.

# Code
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True

        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (
                        dp[i - 1][j]
                        if s[i - 1] == p[j - 2] or p[j - 2] == '.'
                        else False
                    )

        return dp[len(s)][len(p)]
```