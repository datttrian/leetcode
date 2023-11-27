from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Find the minimum path sum from the top-left to the bottom-right corner
        of the grid.

        Parameters:
        - grid (List[List[int]]): The m x n grid filled with non-negative
        numbers.

        Returns:
        - int: The minimum path sum.
        """
        m, n = len(grid), len(grid[0])

        # Initialize the first row and first column with cumulative sums
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        # Calculate the minimum path sum for each cell
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]
