class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # Initialize a 2D DP array to store the matching results
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty pattern matches empty string
        dp[0][0] = True

        # Handle patterns with '*' at the beginning
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Dynamic programming to fill the DP array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[m][n]
