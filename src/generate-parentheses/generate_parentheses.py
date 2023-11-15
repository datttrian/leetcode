from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all valid combinations of parentheses for a given number of
        pairs.

        Summary:
        Generate all valid combinations of parentheses for a given number of
        pairs.

        Description:
        This function uses a backtracking algorithm to explore all possible
        combinations of parentheses. It ensures that at any point in the
        construction of a combination, the number of open parentheses does not
        exceed the given total 'n', and the number of closed parentheses does
        not exceed the number of open parentheses. The result is a list of
        strings representing all valid combinations of parentheses.

        Algorithm:
        The backtracking algorithm explores different paths, adding an open
        parenthesis when the count of open parentheses is less than 'n', and
        adding a closed parenthesis when the count of closed parentheses is
        less than the count of open parentheses. The process continues
        recursively until a valid combination of length '2 * n' is formed.

        Parameters:
        - n (int): The number of pairs of parentheses to generate combinations
        for.

        Returns:
        List[str]: A list of strings representing all valid combinations of
        parentheses.

        Raises:
        N/A

        Complexity:
        The time complexity of this algorithm is O(4^n / sqrt(n)), where 'n'
        is the given number of pairs. The space complexity is O(4^n / sqrt(n))
        as well, considering the number of valid combinations that need to be
        stored.
        """

        def backtrack(s: str = '', left: int = 0, right: int = 0):
            """
            Recursive helper function to generate valid combinations of
            parentheses.

            Parameters:
            - s (str): The current combination being constructed.
            - left (int): The count of open parentheses in the current
            combination.
            - right (int): The count of closed parentheses in the current
            combination.
            """
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        result: List[str] = []  # List to store the generated combinations
        backtrack()  # Start the backtracking process
        return result  # Return the list of valid combinations
