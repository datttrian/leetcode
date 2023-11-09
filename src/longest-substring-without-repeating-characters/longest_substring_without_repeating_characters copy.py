from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Compute the length of the longest substring without repeating
        characters.

        This function uses a sliding window approach to find the maximum
        length of a substring without duplicate characters in a given string.
        It iterates through the string, using a dictionary to store the most
        recent index of each character encountered. When a repeat character is
        found, the left boundary of the window is moved to one past the last
        occurrence of that character.

        Args:
            s (str): The input string to be evaluated.

        Returns:
            int: The length of the longest substring without repeating
            characters.

        Complexity:
            Time: O(n), where n is the length of the string. The function
            iterates through the string once with constant-time operations at
            each step.
            Space: O(min(m, n)), where m is the size of the character set and
            n is the length of the string. In the worst case, the whole string
            might be stored in the dictionary, but typically the size is
            limited by the character set.
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
