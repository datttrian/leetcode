from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Calculate length of the longest substring without repeating characters.

        This method iterates through the given string, utilizing a dictionary
        to track the last index at which each character appears. It uses a
        sliding window approach to maintain a substring where no characters are
        repeated. The length of this window is checked at each step to
        determine if it's the longest one found so far.

        Args:
            s (str): The string to be evaluated.

        Returns:
            int: The length of the longest substring without repeating
            characters.

        Complexity:
            Time: O(n), where n is the length of the string. The method
            iterates through the string once.
            Space: O(min(m, n)), where m is the size of the charset used in
            the string. In the worst case, all characters are unique and m
            equals n.
        """
        # Initialize a dictionary to keep track of the last index of each
        # character.
        char_index_map: Dict[str, int] = {}
        # 'start' marks the beginning of the current substring, 'max_length'
        # is the max substring length found.
        start = max_length = 0

        for i, char in enumerate(s):
            # If the character is already in the dictionary and its last
            # occurrence is within the current window.
            if char in char_index_map and char_index_map[char] >= start:
                # Update 'start' to be one position after the last occurrence
                # of 'char'.
                start = char_index_map[char] + 1

            # Update the last occurrence of 'char' to the current index 'i'.
            char_index_map[char] = i

            # Update 'max_length' to the maximum of its current value or the
            # length of the current window.
            max_length = max(max_length, i - start + 1)

        return max_length
