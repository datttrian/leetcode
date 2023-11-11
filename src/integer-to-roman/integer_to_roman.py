class Solution:
    def intToRoman(self, num: int) -> str:
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
        for i in range(len(symbols)):
            # Repeat the symbol as many times as it fits in the number
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]

        return result
