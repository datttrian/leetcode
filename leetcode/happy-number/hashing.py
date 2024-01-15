class Solution:
    def isHappy(self, n: int) -> bool:
        """Determine if a number is a happy number.

        A happy number is a number that, when replaced by the sum of the
        squares of its digits, eventually leads to the number 1.

        Parameters:
        - n (int): The input number.

        Returns:
        - bool: True if the number is a happy number, False otherwise.
        """
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1
