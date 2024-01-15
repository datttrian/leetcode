class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_squared_digits(num: int) -> int:
            return sum(int(digit) ** 2 for digit in str(num))

        slow, fast = n, sum_squared_digits(n)
        while fast != 1 and slow != fast:
            slow = sum_squared_digits(slow)
            fast = sum_squared_digits(sum_squared_digits(fast))
        return fast == 1
