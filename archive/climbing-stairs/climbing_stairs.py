class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculate the number of distinct ways to climb to the top of a
        staircase.

        Parameters:
        - n (int): The number of steps to reach the top of the staircase.

        Returns:
        - int: The number of distinct ways to climb to the top.
        """
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize an array to store the number of ways to reach each step
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        # Calculate the number of ways for each step from 3 to n
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
