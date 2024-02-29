class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Convert the initial portion of the string to a 32-bit signed integer.

        This method processes the given string and converts it into an integer.
        It handles optional leading white spaces, an optional sign, and
        numerical characters. Non-numeric characters are ignored, and the
        function stops processing upon encountering them. The function also
        handles integer overflow and underflow by clamping the result to the
        range of 32-bit signed integers.

        Parameters:
        s (str): The string to be converted to an integer.

        Returns:
        int: The converted integer. If overflow or underflow occurs, it
        returns INT_MAX (2**31 - 1) or INT_MIN (-2**31), respectively.

        Complexity:
        Time: O(n), where n is the length of the string.
        Space: O(1), as it uses a constant amount of space.

        Example:
        >>> solution = Solution()
        >>> solution.myAtoi("42")
        42
        >>> solution.myAtoi("   -42")
        -42
        >>> solution.myAtoi("4193 with words")
        4193
        >>> solution.myAtoi("words and 987")
        0
        >>> solution.myAtoi("-91283472332")
        -2147483648
        """
        # Define the range of a 32-bit signed integer
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        # Initialize variables
        i = 0
        n = len(s)
        sign = 1
        result = 0

        # Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Check for sign
        if i < n and s[i] in ['-', '+']:
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Convert numbers and stop at the first non-digit
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Check for overflow/underflow and clamp if necessary
            # This check prevents overflow during the calculation.
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result
