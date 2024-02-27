from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.

        Parameters:
        - s (str): The input string.

        Returns:
        - int: The length of the longest substring without repeating
        characters.

        Raises:
        - None: No specific exceptions are raised by this function.
        """
        # Dictionary to store the most recent index of each character
        char_index_map: Dict[str, int] = {}

        # Initialize the left boundary of the current window
        left: int = 0

        # Initialize the length of the longest substring found
        max_length: int = 0

        # Enumerate over each character in the string
        for right, char in enumerate(s):
            # Check if the character has been seen and is within the current
            # window
            if char in char_index_map and char_index_map[char] >= left:
                # Move the left boundary to one past the last occurrence of
                # the current character
                left = char_index_map[char] + 1

            # Update the character's latest index in the dictionary
            char_index_map[char] = right

            # Update the maximum length if the current window size is larger
            max_length = max(max_length, right - left + 1)

        # Return the length of the longest substring found
        return max_length
