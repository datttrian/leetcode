class Solution:
    def reverse(self, x: int) -> int:
        # Check if the number is negative
        sign = -1 if x < 0 else 1
        # Reverse the number and strip the sign
        reversed_num = sign * int(str(abs(x))[::-1])

        # Check if the reversed number is within the 32-bit signed integer
        # range
        if -(2**31) <= reversed_num <= 2**31 - 1:
            return reversed_num
        else:
            return 0
