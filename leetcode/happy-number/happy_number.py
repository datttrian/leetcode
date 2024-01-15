class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num: int) -> int:
            return sum(int(digit) ** 2 for digit in str(num))

        current, next_num = n, get_next(n)
        while next_num != 1 and current != next_num:
            current = get_next(current)
            next_num = get_next(get_next(next_num))
        return next_num == 1
