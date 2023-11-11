class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert an integer to a Roman numeral.

        Parameters:
        - num (int): The input integer to be converted to a Roman numeral.
        Should be in the range 1 to 3999, inclusive.

        Returns:
        - str: The Roman numeral representation of the input integer.

        Methodology:
        This method employs a greedy algorithm to iteratively subtract the
        largest possible values from the input integer. It utilizes a
        predefined set of Roman numeral symbols and their corresponding values
        to construct the resulting Roman numeral.

        Symbol Legend:
        - M: 1000
        - CM: 900
        - D: 500
        - CD: 400
        - C: 100
        - XC: 90
        - L: 50
        - XL: 40
        - X: 10
        - IX: 9
        - V: 5
        - IV: 4
        - I: 1

        Time Complexity:
        The time complexity is O(13 * log(num)), where "num" is the input
        integer. The algorithm iterates through the set of symbols, and in the
        worst case, the while loop may run log(num) times for each symbol.

        Space Complexity:
        The space complexity is O(1) as the space required for the algorithm
        is constant regardless of the input size. It primarily uses the
        "result" string and the predefined sets of symbols and values.
        """
        # Define the symbols and their values
        symbols = [
            'M',
            'CM',
            'D',
            'CD',
            'C',
            'XC',
            'L',
            'XL',
            'X',
            'IX',
            'V',
            'IV',
            'I',
        ]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        # Initialize an empty string to store the Roman numeral
        result = ''

        # Iterate through the symbols and values
        for symbol, value in zip(symbols, values):
            # Repeat the symbol as many times as it fits in the number
            while num >= value:
                result += symbol
                num -= value

        return result
