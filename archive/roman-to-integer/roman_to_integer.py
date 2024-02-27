class Solution:
    def romanToInt(self, s: str) -> int:
        """Convert a Roman numeral string to an integer.

        The conversion is achieved by iterating through the input string
        from right to left, convert the character to number value, add
        or subtract the number to the result based on Rules of Roman Numerals

        Args:
            s (str): A Roman numeral string consisting of uppercase letters.

        Returns:
            int: The integer value corresponding to the input Roman numeral
            string.

        Raises:
            None: It is guaranteed that s is a valid Roman numeral.
        """
        # Dictionary of roman symbols and their values
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # Variable to store the accumulated value
        result = 0

        # Variable to keep track of the previous value during iteration
        prev_value = 0

        # Iterate through the reversed Roman string
        for _, char in enumerate(reversed(s)):
            # Retrieve the integer value of the current Roman symbol
            current_value = roman_dict[char]

            # When the next number is smaller than the previous one
            if current_value < prev_value:
                # It is subtracted from the total
                result -= current_value
            else:
                # When the next number is bigger or equal to the current number
                # Add the number to the total
                result += current_value

            # Update the previous value for the next iteration
            prev_value = current_value

        # Return the final accumulated integer value
        return result