class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """Perform integer division of the given dividend by the divisor.

        This method calculates the integer division of the given dividend by
        the divisor. It handles cases such as division by 1, division by -1,
        and general integer division.

        Args:
        - dividend (int): The number to be divided.
        - divisor (int): The number by which the dividend is divided.

        Returns:
        int: The result of the integer division.
        """
        int_max = 2**31 - 1
        int_min = -(2**31)

        if dividend == 0:
            return 0
        if divisor == 1:
            return min(max(int_min, dividend), int_max)
        if divisor == -1:
            return min(max(int_min, -dividend), int_max)

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            dividend -= divisor
            quotient += 1

        return -quotient if negative else quotient
