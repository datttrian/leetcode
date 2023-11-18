class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Convert the input string into a zigzag pattern with a given number of
        rows.

        Parameters:
        - s (str): The input string to be converted.
        - numRows (int): The number of rows in the zigzag pattern.

        Returns:
        - str: The zigzag pattern representation of the input string.

        Raises:
        - None
        """
        # Edge case: When the zigzag pattern is not applicable, return the
        # original string
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize a list of strings to represent each row of the zigzag
        # pattern
        rows = [''] * numRows

        # Start at the first row
        current_row = 0

        # This flag indicates whether we are moving down or up in the zigzag
        going_down = False

        # Iterate over each character in the string
        for char in s:
            # Append the character to the string corresponding to the current
            # row
            rows[current_row] += char

            # If we are at the top or bottom of a zigzag, reverse the direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # Move to the next row in the zigzag pattern
            current_row += 1 if going_down else -1

        # Concatenate all rows to form the final zigzag pattern string
        return ''.join(rows)
