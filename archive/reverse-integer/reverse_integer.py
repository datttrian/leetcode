class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1

        reversed_num = sign * int(str(abs(x))[::-1])

        if -(2**31) <= reversed_num <= 2**31 - 1:
            return reversed_num
        return 0
