class Solution:
    def isValid(self, s: str) -> bool:
        # Base case: If `s` is empty, it is considered valid
        if not s:
            return True

        # Initialize the length of the string and an index to traverse it
        length = len(s)
        index = 0

        # Define a dictionary to map each opening parenthesis to its corresponding closing parenthesis
        matching_parentheses = {"(": ")", "{": "}", "[": "]"}

        # Loop through the string until the second last character
        while index < length - 1:
            # Check each pair of characters for a matching set of parentheses
            for open_paren, close_paren in matching_parentheses.items():
                # If a matching pair is found
                if s[index] == open_paren and s[index + 1] == close_paren:
                    # Create a new string without the matched parentheses
                    new_string = s[:index] + s[index + 2:]
                    # Recursively check if the new string is valid
                    return self.isValid(new_string)
            # Move to the next character in the string
            index += 1

        # If no valid pairs were found, return False
        return False


solution = Solution()
print(solution.isValid(s="()"))
print(solution.isValid(s="()[]{}"))
print(solution.isValid(s="(]"))
