from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all valid combinations of parentheses with a given number of
        pairs.

        Summary:
        Generates all valid combinations of parentheses for a given number of
        pairs.

        Description:
        This method uses a backtracking algorithm to explore and construct all
        possible combinations of well-formed parentheses. It maintains counts
        of open and closed parentheses to ensure validity and completeness of
        the generated combinations.

        Algorithm:
        1. Start with an empty string and counts of open and closed
        parentheses set to zero.
        2. Recursively explore two possibilities:
           a. Add an open parenthesis if the count of open parentheses used is
           less than n.
           b. Add a closed parenthesis if the count of closed parentheses used
           is less than the count of open parentheses.
        3. Base case: When the length of the combination is equal to twice the
        number of pairs, add it to the result.
        4. Repeat the process until all valid combinations are generated.

        Parameters:
        - n (int): The number of pairs of parentheses to be used.

        Returns:
        List[str]: A list of strings representing all valid combinations of
        parentheses.

        Raises:
        No explicit exceptions are raised.

        Complexity:
        - Time: O(4^n / sqrt(n)), as each valid
        combination can have up to 2n characters, and at each step, we make
        two recursive calls.
        - Space: O(4^n / sqrt(n)) as there can be a total of 4^n / sqrt(n)
        valid combinations in the output list.
        """

        def backtrack(s: str = '', left: int = 0, right: int = 0):
            """
            Backtrack to generate valid combinations of parentheses.

            Parameters:
            - s (str): The current combination of parentheses.
            - left (int): The count of open parentheses used so far.
            - right (int): The count of closed parentheses used so far.
            """
            # Base case: If the combination is complete, add it to the result
            if len(s) == 2 * n:
                result.append(s)
                return

            # Recursive cases:
            # 1. Add an open parenthesis if the count of open parentheses used
            # is less than n
            if left < n:
                backtrack(s + '(', left + 1, right)
            # 2. Add a closed parenthesis if the count of closed parentheses
            # used is less than the count of open parentheses
            if right < left:
                backtrack(s + ')', left, right + 1)

        # List to store valid combinations of parentheses
        result: List[str] = []

        # Start the backtracking process
        backtrack()

        # Return the final list of valid combinations
        return result
