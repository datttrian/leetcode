from math import factorial
from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Return the k-th permutation sequence for the set [1, 2, ..., n].

        Parameters:
        - n (int): The positive integer representing the size of the set.
        - k (int): The position of the desired permutation.

        Returns:
        - str: The k-th permutation sequence.
        """
        k -= 1  # Convert k to zero-based index
        result: List[str] = []
        numbers: List[int] = list(range(1, n + 1))

        for i in range(n, 0, -1):
            index, k = divmod(k, factorial(i - 1))
            result.append(str(numbers.pop(index)))

        return ''.join(result)
