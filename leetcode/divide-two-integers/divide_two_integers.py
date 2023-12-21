class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """Divide two integers and return the quotient.

        The division is performed using long division, taking into account
        the sign of the dividend and divisor. The function handles edge
        cases such as division by zero and ensures that the result is within
        the 32-bit signed integer range.

        Args:
            dividend (int): The integer to be divided.
            divisor (int): The integer by which the dividend is divided.

        Returns:
            int: The quotient of the division.

        Raises:
            None: The function is designed to handle all valid inputs.
        """
        # Define constants for maximum and minimum 32-bit signed integers
        int_max = 2**31 - 1
        int_min = -(2**31)

        # Handle division by zero
        if divisor == 0:
            return int_max if dividend > 0 else int_min

        # Handle case where dividend is zero
        if dividend == 0:
            return 0

        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Take the absolute values of dividend and divisor for calculation
        dividend, divisor = abs(dividend), abs(divisor)

        # Initialize quotient
        quotient = 0

        # Perform long division
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1

            # Double divisor and multiple until it exceeds dividend
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            # Subtract the doubled divisor from the remaining dividend
            dividend -= temp_divisor
            # Add the multiple to the quotient
            quotient += multiple

        # Apply the sign to the quotient
        quotient *= sign

        # Ensure the result is within the 32-bit signed integer range
        return min(max(quotient, int_min), int_max)