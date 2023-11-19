class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle special cases
        if dividend == 0:
            return 0
        if divisor == 1:
            return min(max(INT_MIN, dividend), INT_MAX)
        if divisor == -1:
            return min(max(INT_MIN, -dividend), INT_MAX)

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Convert both dividend and divisor to positive
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        # Apply the sign to the result
        return -quotient if negative else quotient
