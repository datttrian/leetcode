class Solution:
    def intToRoman(self, num: int) -> str:
        # Dictionary in descending order including more than one symbol values
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

        # Variable to store the final Roman string
        result = ""

        # Iterate through the dictionary
        for value, symbol in roman_extend_dict.items():
            # Determine how many times the value can be subtracted from num
            count, num = divmod(num, value)

            # Append the corresponding Roman numeral to the result string
            result += symbol * count

        # Return the final Roman string
        return result
