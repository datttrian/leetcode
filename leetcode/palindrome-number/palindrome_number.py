class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check if the number is negative or ends with zero except 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Variable to store the reversed number
        reversed_num = 0

        # Save the original number for comparison
        original_num = x

        # Reverse the digits of the number
        while x > 0:
            x, digit = divmod(x, 10)
            reversed_num = reversed_num * 10 + digit

        # Check if the reversed number is equal to the original number
        return reversed_num == original_num
