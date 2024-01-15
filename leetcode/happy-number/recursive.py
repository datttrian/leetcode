class Solution:
    def isHappy(self, n: int) -> bool:
        def is_happy_recursive(n: int, seen: set[int]) -> bool:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            return is_happy_recursive(get_next(n), seen)

        def get_next(number: int) -> int:
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit**2
            return total_sum

        seen: set[int] = set()
        return is_happy_recursive(n, seen)
