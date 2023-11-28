class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Special cases: Negative numbers and numbers ending with 0 are not
        # palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Initialize variables to store the reversed number and the original
        # number
        reversed_num = 0
        original_num = x

        # Reverse the digits of the original number
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        # Check if the reversed number equals the original number, indicating
        # a palindrome
        return reversed_num == original_num
