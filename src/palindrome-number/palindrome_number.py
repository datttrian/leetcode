class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Determine whether a given integer is a palindrome.

        A palindrome is a number that reads the same backward as forward.

        Parameters:
        - x (int): The integer to be checked for palindrome property.

        Returns:
        bool: True if the input integer is a palindrome, False otherwise.

        Special cases:
        - Negative numbers are not palindromes.
        - Numbers ending with 0 (except 0 itself) are not palindromes.

        Time Complexity:
        O(log10(x)) - The number of iterations in the while loop is
        proportional to the number of digits in the input integer.

        Space Complexity:
        O(1) - Constant space is used to store the reversed number and the
        original number.

        Example:
        ```
        solution = Solution()
        result = solution.isPalindrome(121)
        print(result)  # Output: True
        ```
        """
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
