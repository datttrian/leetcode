class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary mapping Roman numerals to their corresponding integer
        # values
        roman_dict: dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # Initialize result and keep track of the previous value
        result: int = 0
        prev_value: int = 0

        # Iterate through the string in reverse order
        for char in reversed(s):
            current_value: int = roman_dict[char]

            # If the current value is less than the previous value, subtract
            # it; otherwise, add it
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value

            # Update the previous value for the next iteration
            prev_value = current_value

        # Return the final result
        return result
