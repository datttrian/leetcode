class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        is_negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp_divisor, temp_quotient = divisor, 1

            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                temp_quotient <<= 1

            dividend -= temp_divisor
            quotient += temp_quotient

        if is_negative:
            quotient = -quotient

        return min(max(quotient, INT_MIN), INT_MAX)
