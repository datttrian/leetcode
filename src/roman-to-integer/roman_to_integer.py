class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert a Roman numeral string to an integer.

        This method takes a Roman numeral string as input and converts it into
        its corresponding integer representation. The Roman numerals are
        represented by characters ('I', 'V', 'X', 'L', 'C', 'D', 'M'), and the
        conversion is performed by iterating through the input string and
        applying the rules of Roman numeral representation.

        Parameters:
        - s (str): The input Roman numeral string. It should be a non-empty
        string containing valid Roman numeral characters. The length of the
        string should be between 1 and 15, inclusive.

        Returns:
        - int: The integer representation of the input Roman numeral string.

        Complexity:
        - Time: O(n), where n is the length of the input string. The algorithm
        iterates through each character of the string once.
        - Space: O(1), as the space required is constant. The dictionary and
        variables used for computation do not scale with the input size.

        Example:
        ```python
        solution = Solution()
        result = solution.romanToInt("III")
        print(result)  # Output: 3
        ```

        Note:
        The Roman numeral input is assumed to be valid, and no error handling
        is implemented for invalid inputs.
        """
        # Dictionary mapping Roman numerals to their corresponding values
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        # Initialize the result and keep track of the previous Roman numeral
        # value
        result = 0
        prev_value = 0

        # Iterate through the input string in reverse order
        for char in reversed(s):
            current_value = roman_dict[char]
            # Compare the current value with the previous one
            if current_value < prev_value:
                # If the current value is smaller than the previous, subtract
                # it
                result -= current_value
            else:
                # If the current value is greater or equal to the previous,
                # add it
                result += current_value
            # Update the previous value for the next iteration
            prev_value = current_value

        # Return the final result
        return result
