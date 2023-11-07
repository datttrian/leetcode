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
        char_index_map: Dict[str, int] = {}
        left: int = 0  # Initial left boundary of the sliding window
        max_length: int = 0  # Length of the longest substring found

        for right, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1  # Adjust the left boundary
            char_index_map[char] = right  # Update the character's index
            max_length = max(
                max_length,
                right - left + 1,
            )  # Update max_length if current window is larger

        return max_length
