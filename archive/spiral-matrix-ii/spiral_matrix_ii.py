from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Generate an n x n matrix filled with elements from 1 to n^2 in spiral
        order.

        Parameters:
        - n (int): The positive integer representing the size of the matrix.

        Returns:
        - List[List[int]]: The generated spiral matrix.
        """
        matrix = [[0] * n for _ in range(n)]

        num = 1
        left, right, top, bottom = 0, n - 1, 0, n - 1

        while num <= n * n:
            # Traverse from left to right
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1

            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # Traverse from right to left
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix
