class Solution:
    """
    A class that provides a method for determining whether a given integer is a palindrome.

    Summary:
    --------
    The `isPalindrome` method checks if an input integer is a palindrome. A palindrome
    is a number that reads the same backward as forward.

    Description:
    ------------
    The method handles special cases, such as negative numbers and numbers ending with
    0 (excluding 0 itself), which are not considered palindromes. It then uses a
    loop to reverse the digits of the input number and compares the reversed number
    with the original number to determine if it's a palindrome.

    Parameters:
    -----------
    x : int
        The input integer to be checked for palindrome property.

    Returns:
    --------
    bool
        Returns True if the input integer is a palindrome, and False otherwise.

    Raises:
    -------
    No explicit exceptions are raised in this implementation.

    Complexity:
    ------------
    Time Complexity: O(log10(x))
        The time complexity is logarithmic, as the number of digits in the input
        integer determines the number of iterations in the loop.

    Space Complexity: O(1)
        The space complexity is constant, as only a few variables are used
        irrespective of the size of the input integer.

    Comments:
    ---------
    The approach of reversing the digits avoids the need to convert the integer to
    a string for comparison, making it more memory-efficient. The special cases are
    handled at the beginning to improve performance by skipping unnecessary
    computations.
    """

    def isPalindrome(self, x: int) -> bool:
        # Special cases: Negative numbers and numbers ending with 0 are not
        # palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0
        original_num = x

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        # If the reversed number equals the original number, it's a palindrome
        return reversed_num == original_num
