class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        # Handle special cases
        if divisor == 0:
            return INT_MAX if dividend > 0 else INT_MIN
        if dividend == 0:
            return 0

        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Convert both dividend and divisor to positive values
        dividend, divisor = abs(dividend), abs(divisor)

        # Initialize quotient
        quotient = 0

        # Bitwise division
        while dividend >= divisor:
            # Use left shift to find the largest multiple of divisor that can
            # be subtracted from dividend
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            # Subtract the multiple of divisor from dividend and update the
            # quotient
            dividend -= temp_divisor
            quotient += multiple

        # Apply the sign to the quotient
        quotient *= sign

        # Handle overflow
        return min(max(quotient, INT_MIN), INT_MAX)
