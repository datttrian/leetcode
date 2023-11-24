class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 0:
            return 0

        # dp[i] represents the number of unique BST's with i nodes
        dp = [0] * (n + 1)

        # There is one unique BST with 0 node
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                # dp[i] is the sum of all products of dp[j-1] and dp[i-j]
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]
