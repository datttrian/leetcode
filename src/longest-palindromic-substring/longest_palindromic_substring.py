class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        n = len(s)

        is_palindrome = [[False] * n for _ in range(n)]

        start = 0
        max_length = 1

        for i in range(n):
            is_palindrome[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = True
                start = i
                max_length = 2

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = True

                    if length > max_length:
                        start = i
                        max_length = length

        return s[start : start + max_length]
