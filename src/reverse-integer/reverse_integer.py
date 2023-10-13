class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        sign = 1 if x >= 0 else -1
        x = abs(x)

        r = 0
        while x:
            if r > INT_MAX // 10 or r < INT_MIN // 10:
                return 0
            r = r * 10 + x % 10
            x = x // 10
        return sign * r
