class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_squared_digit(num: int) -> int:
            return sum(int(digit) ** 2 for digit in str(num))

        current, next_num = n, sum_squared_digit(n)
        while next_num not in (1, current):
            current = sum_squared_digit(current)
            next_num = sum_squared_digit(sum_squared_digit(next_num))
        return next_num == 1
