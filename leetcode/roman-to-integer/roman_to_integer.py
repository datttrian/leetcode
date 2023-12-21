class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert a Roman numeral to an integer.

        Parameters:
        s (str): A string representing a Roman numeral.

        Returns:
        int: The integer representation of the Roman numeral.
        """

        # Define a dictionary to map numerals to integer
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # Initialize the result and the previous value
        result = 0
        prev_value = 0

        # Iterate over the string in reverse order
        for char in reversed(s):
            # Get the integer value of the current Roman numeral
            current_value = roman_dict[char]

            # If the current value is less than the previous value
            if current_value < prev_value:
                # Subtract it from the result
                result -= current_value
            else:
                # Otherwise, add the current value to the result
                result += current_value

            # Update the previous value for the next iteration
            prev_value = current_value

        # Return the final result
        return result
