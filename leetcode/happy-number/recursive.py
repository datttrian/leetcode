class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num: int) -> int:
            return sum(int(digit) ** 2 for digit in str(num))

        def is_happy_recursive(num: int, seen: set[int]) -> bool:
            if num == 1:
                return True
            if num in seen:
                return False

            seen.add(num)
            next_num = get_next(num)
            return is_happy_recursive(next_num, seen)

        seen_set: set[int] = set()
        return is_happy_recursive(n, seen_set)
