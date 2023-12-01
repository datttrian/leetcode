class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        digits = []
        while x > 0:
            digit = x % 10
            x //= 10
            digits.append(digit)

        n = len(digits)
        for i in range(n // 2):
            if digits[i] != digits[n - 1 - i]:
                return False

        return True
