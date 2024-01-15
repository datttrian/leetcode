class Solution:
    def isHappy(self, n: int) -> bool:
        """Determines whether a given number is a happy number.

        Parameters:
        - n (int): The input number to check for happiness.

        Returns:
        - bool: True if the number is a happy number, False otherwise.
        """

        def get_next(num: int) -> int:
            """Calculates the next number in the sequence for determining
            happiness.

            Parameters:
            - num (int): The current number in the sequence.

            Returns:
            - int: The next number in the sequence.
            """
            return sum(int(digit) ** 2 for digit in str(num))

        current, next_num = n, get_next(n)
        while next_num not in (1, current):
            current = get_next(current)
            next_num = get_next(get_next(next_num))
        return next_num == 1
