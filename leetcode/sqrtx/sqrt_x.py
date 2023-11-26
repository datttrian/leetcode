class Solution:
    def mySqrt(self, x: int) -> int:
        if x in (0, 1):
            return x

        left, right = 1, x // 2

        while left <= right:
            mid = left + (right - left) // 2
            mid_squared = mid * mid

            if mid_squared == x:
                return mid
            if mid_squared < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
