class Solution:
    def romanToInt(self, s: str) -> int:
        """Convert a Roman numeral to an integer.

        This method takes a Roman numeral as input and calculates its
        corresponding integer value using the Roman numeral to integer
        mapping. The input Roman numeral should be a valid representation
        using the characters 'I', 'V', 'X', 'L', 'C', 'D', and 'M'.

        The algorithm processes the Roman numeral in reverse order, starting
        from the rightmost character. It compares the current character's
        value with the previous character's value. If the current value is
        less than the previous value, it subtracts the current value from the
        result; otherwise, it adds the current value to the result.

        Args:
        - s (str): The input Roman numeral as a string.

        Returns:
        int: The integer equivalent of the input Roman numeral.

        Returns:
        int: The integer equivalent of the input Roman numeral.

        Raises:
        - None since It is **guaranteed** that `s` is a valid roman numeral in
        the range `[1, 3999]`.
        """
        # Dictionary to map Roman numerals to their corresponding values
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # Initialize the result and the previous value variables
        result = 0
        prev_value = 0

        # Iterate through the reversed string
        for char in reversed(s):
            # Retrieve the numeric value of the current Roman numeral
            current_value = roman_dict[char]

            # Check if the current value is less than the previous value
            if current_value < prev_value:
                # If true, subtract the current value from the result
                result -= current_value
            else:
                # If false, add the current value to the result
                result += current_value

            # Update the previous value for the next iteration
            prev_value = current_value

        # Return the final result
        return result
