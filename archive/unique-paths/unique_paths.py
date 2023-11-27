class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Return the number of possible unique paths from the top-left to the
        bottom-right corner.

        Parameters:
        - m (int): The number of rows in the grid.
        - n (int): The number of columns in the grid.

        Returns:
        - int: The number of unique paths.
        """
        # There is only one path for a grid with one row or one column
        if m == 1 or n == 1:
            return 1

        dp = [[0] * n for _ in range(m)]

        # Initialize the first row and first column with 1
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # Calculate unique paths for each cell
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
