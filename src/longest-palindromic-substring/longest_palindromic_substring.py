class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring in the input string.

        This method utilizes dynamic programming to efficiently determine the
        longest palindromic substring in the given string. It constructs a
        table to store whether a substring is a palindrome or not, allowing it
        to avoid redundant computations.

        Args:
            s (str): The input string in which to find the longest palindromic
                     substring.

        Returns:
            str: The longest palindromic substring found in the input string.

        Complexity:
            - Time: O(n^2) where 'n' is the length of the input string 's'.
              The most time-consuming part of the algorithm is constructing
              the 'is_palindrome' table.
            - Space: O(n^2) due to the 'is_palindrome' table, which stores the
              results for all possible substrings.

        Example:
        >>> solution = Solution()
        >>> solution.longestPalindrome("babad")
        'bab'  # 'aba' is also a valid answer.

        Note:
        - The method handles empty input strings gracefully, returning an empty
          string.
        - In case of multiple valid answers, this method returns the one with
          the earliest occurrence in the input string.
        """
        if not s:
            return ''

        n = len(s)
        # Create a table to store whether a substring is a palindrome or not.
        is_palindrome = [[False] * n for _ in range(n)]

        start = (
            0  # Start index of the longest palindromic substring found so far.
        )
        max_length = (
            1  # Length of the longest palindromic substring found so far.
        )

        # All substrings of length 1 are palindromes.
        for i in range(n):
            is_palindrome[i][i] = True

        # Check for palindromes of length 2.
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = True
                start = i
                max_length = 2

        # Check for palindromes of length 3 or more.
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1  # Ending index of the current substring.

                # Check if the current substring is a palindrome and its inner
                # substring is also a palindrome.
                if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = True

                    # Update the longest palindromic substring if necessary.
                    if length > max_length:
                        start = i
                        max_length = length

        return s[start : start + max_length]
