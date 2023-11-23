class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False

        n = len(s1)
        dp = [[[False] * n for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[0][i][j] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                for j in range(n - length + 1):
                    for k in range(1, length):
                        if (
                            dp[k - 1][i][j]
                            and dp[length - k - 1][i + k][j + k]
                        ) or (
                            dp[k - 1][i][j + length - k]
                            and dp[length - k - 1][i + k][j]
                        ):
                            dp[length - 1][i][j] = True
                            break

        return dp[n - 1][0][0]
