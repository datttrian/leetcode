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

        def get_next(num: int) -> int:
            """Calculate the next number in the happy number sequence.

            Parameters:
            - num (int): The current number in the sequence.

            Returns:
            - int: The next number in the sequence.
            """
            return sum(int(digit) ** 2 for digit in str(num))

        def is_happy_recursive(num: int, seen: set[int]) -> bool:
            """Recursively check if a number is a happy number.

            Parameters:
            - num (int): The current number in the recursion.
            - seen (set[int]): A set to track numbers seen during recursion.

            Returns:
            - bool: True if the number is a happy number, False otherwise.
            """
            if num == 1:
                return True
            if num in seen:
                return False

            seen.add(num)
            next_num = get_next(num)
            return is_happy_recursive(next_num, seen)

        seen_set: set[int] = set()
        return is_happy_recursive(n, seen_set)
