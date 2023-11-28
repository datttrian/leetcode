class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        if dividend == 0:
            return 0
        if divisor == 1:
            return min(max(INT_MIN, dividend), INT_MAX)
        if divisor == -1:
            return min(max(INT_MIN, -dividend), INT_MAX)

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            dividend -= divisor
            quotient += 1

        return -quotient if negative else quotient
