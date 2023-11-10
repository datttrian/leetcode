class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Determine if the input string 's' matches the given pattern 'p'
        with support for '.' (matches any single character) and '*'
        (matches zero or more of the preceding element).

        Args:
        - s (str): The input string to be matched.
        - p (str): The pattern to be used for matching.

        Returns:
        bool: True if the entire input string matches the pattern, False
        otherwise.

        Examples:
        1. obj = Solution()
           obj.isMatch("aa", "a")   # Output: False
        2. obj = Solution()
           obj.isMatch("aa", "a*")  # Output: True
        3. obj = Solution()
           obj.isMatch("ab", ".*")  # Output: True

        Complexity:
        Time: O(m * n), where m is the length of the input string 's' and n is
        the length of the pattern 'p'.
        Space: O(m * n), for the 2D array 'dp' used for dynamic programming.
        """
        # Create a 2D array to store the intermediate results of matching
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # Empty pattern matches empty string
        dp[0][0] = True

        # Handle patterns with '*' at the beginning
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                # If '*' is at the beginning, consider zero occurrences of the
                # preceding element
                dp[0][j] = dp[0][j - 2]

        # Dynamic programming to fill the dp array
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    # If current characters match or pattern has '.', take
                    # value from diagonal (top-left)
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # If '*' is encountered, consider either zero occurrences
                    # or match with the previous character
                    dp[i][j] = dp[i][j - 2] or (
                        dp[i - 1][j]
                        if s[i - 1] == p[j - 2] or p[j - 2] == '.'
                        else False
                    )

        # The result is stored in the bottom-right cell of the dp array
        return dp[len(s)][len(p)]
