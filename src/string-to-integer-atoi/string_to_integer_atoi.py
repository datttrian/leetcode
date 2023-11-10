class Solution:
    def myAtoi(self, s: str) -> int:
        # Define the range of a 32-bit signed integer
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        # Initialize variables
        i = 0
        n = len(s)
        sign = 1
        result = 0

        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check for sign
        if i < n and s[i] in ['-', '+']:
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. Convert numbers and stop at the first non-digit
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # 4. Check for overflow/underflow and clamp if necessary
            if (
                result > (INT_MAX - digit) // 10
            ):  # Checking this way to prevent overflow
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result
