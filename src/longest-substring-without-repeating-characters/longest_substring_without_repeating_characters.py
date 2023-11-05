from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map: Dict[str, int] = {}
        start = max_length = 0

        for i, char in enumerate(s):
            # If the character is found in the map and
            # is inside the current window
            if char in char_index_map and char_index_map[char] >= start:
                # Move the start to one position ahead of the last occurrence
                # to avoid repeating character
                start = char_index_map[char] + 1

            # Update the last seen index of the character
            char_index_map[char] = i

            # Calculate the maximum length by comparing the current length and
            # the previously stored maximum length
            max_length = max(max_length, i - start + 1)

        return max_length
