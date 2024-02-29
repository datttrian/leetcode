from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Return all elements of the matrix in spiral order.

        Parameters:
        - matrix (List[List[int]]): The input matrix.

        Returns:
        - List[int]: Elements of the matrix in spiral order.
        """
        result: List[int] = []

        while matrix:
            result += matrix.pop(0)  # Move from left to right

            if matrix and matrix[0]:  # Move from top to bottom
                for row in matrix:
                    result.append(row.pop())

            if matrix:  # Move from right to left
                result += matrix.pop()[::-1]

            if matrix and matrix[0]:  # Move from bottom to top
                for row in matrix[::-1]:
                    result.append(row.pop(0))

        return result
