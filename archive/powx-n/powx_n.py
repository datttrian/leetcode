class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        powx: float = 1
        while n:
            if n & 1:
                powx *= x
            x *= x
            n >>= 1
        return powx
