class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Convert a string into a specific zigzag pattern on numRows and reads
        it line by line.

        The function simulates writing this string in a zigzag pattern (like
        the letters of a sawtooth shape) and reads it line by line. This is
        particularly useful for encryption algorithms like the rail fence
        cipher.

        Args:
            s (str): The input string to be written in the zigzag pattern.
            numRows (int): The number of rows in the zigzag pattern.

        Returns:
            str: The string as it is read line by line after being written in
            a zigzag pattern.

        Complexity:
            Time: O(n), where n is the length of the input string, since the
            function iterates over all characters once.

            Space: O(n), where n is the length of the input string, due to the
            space required to store the zigzag pattern across numRows which
            collectively will not exceed the length of the input string.
        """
        # Edge case: When the zigzag pattern is not applicable, return
        # original string
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize a list of strings to represent each row of the zigzag
        # pattern
        rows = [''] * numRows
        current_row = 0  # Start at the first row

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
