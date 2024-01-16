class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        pow_x: float = 1
        while n:
            if n & 1:
                pow_x *= x
            x *= x
            n >>= 1
        return pow_x
