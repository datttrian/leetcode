class Solution:
    def romanToInt(self, s: str) -> int:
        """Convert a Roman numeral string to an integer.

        The function takes a Roman numeral string as input and returns its
        corresponding integer value. Roman numerals are represented by
        combinations of the symbols 'I', 'V', 'X', 'L', 'C', 'D', and 'M',
        where each symbol has a specific numeric value. The numeral string is
        processed from right to left, and the values are accumulated based on
        the rules of Roman numeral representation.

        Args:
            s (str): A Roman numeral string consisting of uppercase letters.

        Returns:
            int: The integer value corresponding to the input Roman numeral
            string.

        Raises:
            None: It is guaranteed that s is a valid roman numeral in the
            range [1, 3999].
        """
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        prev_value = 0

        for _, char in enumerate(reversed(s)):
            current_value = roman_dict[char]

            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value

            prev_value = current_value

        return result
