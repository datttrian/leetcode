from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if the input string has valid bracket pairs.

        Summary:
        Given a string containing only parentheses, brackets, and curly braces,
        this method checks if the brackets are correctly paired.

        Description:
        This method uses a stack to keep track of opening brackets as it
        iterates through the input string. For each character, it checks if it
        is an opening bracket, a closing bracket, or neither. If it's an
        opening bracket, it is pushed onto the stack. If it's a closing
        bracket, it checks if the stack is empty or if the top of the stack
        matches the corresponding opening bracket. If neither condition is
        met, the brackets are not valid, and the method returns False. If the
        character is neither an opening nor a closing bracket, the method
        returns False.

        Algorithm:
        1. Initialize an empty stack to keep track of opening brackets.
        2. Define a dictionary (bracket_pairs) to store the bracket pairs for
        quick lookup.
        3. Iterate through each character in the input string.
            a. If the character is an opening bracket, push it onto the stack.
            b. If the character is a closing bracket:
                - Check if the stack is empty or if the top of the stack does
                not match the corresponding opening bracket. If so, return
                False.
            c. If the character is neither an opening nor a closing bracket,
            return False.
        4. After iterating through the entire string, check if the stack is
        empty.
            - If it is, all opening brackets have been matched with their
            corresponding closing brackets. Return True; otherwise, return
            False.

        Parameters:
        - s (str): The input string containing parentheses, brackets, and
        curly braces.

        Returns:
        - bool: True if the brackets in the input string are valid, False
        otherwise.

        Raises:
        No explicit exceptions are raised.

        Complexity:
        - Time: O(n), where n is the length of the input string.
        - Space: O(n), where n is the maximum number of opening brackets that
        can be stored in the stack.
        """
        # Initialize an empty stack to keep track of opening brackets.
        stack: List[str] = []

        # Define a dictionary to store the bracket pairs for quick lookup.
        bracket_pairs = {')': '(', '}': '{', ']': '['}

        # Iterate through each character in the input string.
        for char in s:
            # If the character is an opening bracket, push it onto the stack.
            if char in bracket_pairs.values():
                stack.append(char)
            # If the character is a closing bracket:
            elif char in bracket_pairs.keys():
                # Check if the stack is empty or if the top of the stack does
                # not match
                # the corresponding opening bracket.
                if not stack or stack.pop() != bracket_pairs[char]:
                    return False
            # If the character is neither an opening nor a closing bracket,
            # return False.
            else:
                return False

        # After iterating through the entire string, check if the stack is
        # empty.
        # If it is, all opening brackets have been matched with their
        # corresponding closing brackets.
        return not stack
