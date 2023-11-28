class Solution:
    def intToRoman(self, num: int) -> str:
        """Convert an integer to a Roman numeral string.

        The integer is converted into its Roman numeral representation based
        on the rules of Roman numeral construction. The conversion is achieved
        by iterating through a dictionary of integer-symbol pairs in descending
        order, subtracting the largest possible values from the input number.

        Args:
            num (int): An integer in the range [1, 3999] to be converted to
            a Roman numeral.

        Returns:
            str: The Roman numeral representation of the input integer.

        Raises:
            None: It is guaranteed that num is within the valid range.
        """
        # Dictionary mapping integer values to Roman numeral symbols
        roman_extend_dict = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        # Variable to store the final Roman numeral string
        result = ""

        # Iterate through the dictionary in descending order
        for value, symbol in roman_extend_dict.items():
            # Determine how many times the value can be subtracted from num
            count, num = divmod(num, value)

            # Append the corresponding Roman numeral to the result string
            result += symbol * count

        # Return the final Roman numeral string
        return result
