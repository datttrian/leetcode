from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Return the number of possible unique paths from the top-left to the
        bottom-right corner, considering obstacles in the grid.

        Parameters:
        - obstacleGrid (List[List[int]]): The grid with obstacles marked as 1
        and open spaces as 0.

        Returns:
        - int: The number of unique paths.
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # If the start or end point has an obstacle, no path is possible
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        # Initialize the first row and first column with 1 if there is no
        # obstacle
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]

        # Calculate unique paths for each cell
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
