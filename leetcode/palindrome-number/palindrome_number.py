class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        stack = []
        original_x = x

        while x > 0:
            digit = x % 10
            stack.append(digit)
            x //= 10

        while original_x > 0 and stack:
            digit = stack.pop()
            if digit != original_x % 10:
                return False
            original_x //= 10

        return not stack
