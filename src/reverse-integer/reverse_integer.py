class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse an integer.

        This method takes an integer x and returns its reverse. If the
        reversed integer overflows and is not within the 32-bit signed integer
        range, 0 is returned. The function handles both positive and negative
        integers.

        Parameters:
        x (int): An integer, which could be positive or negative.

        Returns:
        int: The reversed integer if it falls within the 32-bit signed integer
        range, otherwise 0.

        Raises:
        ValueError: If x is not an integer.

        Complexity:
        Time: O(n), where n is the number of digits in x. This is because the
        method converts the integer to a string and iterates over its
        characters.
        Space: O(n), as it creates a string of length n for the
        reversal process.

        Example:
        >>> solution = Solution()
        >>> solution.reverse(123)
        321
        >>> solution.reverse(-123)
        -321
        >>> solution.reverse(120)
        21
        >>> solution.reverse(0)
        0
        """
        # Determine the sign of the input number. If it's negative, sign will
        # be -1, otherwise 1.
        sign = -1 if x < 0 else 1

        # Convert the absolute value of the input number to a string, reverse
        # it, and then convert back to an integer. Apply the original sign.
        reversed_num = sign * int(str(abs(x))[::-1])

        # Check if the reversed number is within the 32-bit signed integer
        # range.
        # The range is from -2^31 to 2^31 - 1.
        if -(2**31) <= reversed_num <= 2**31 - 1:
            return reversed_num
        else:
            # If the number is outside the range, return 0.
            return 0
