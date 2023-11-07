from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map: Dict[
            str,
            int,
        ] = {}  # Maps characters to their latest indices
        left: int = 0  # Left boundary of the window
        max_length: int = (
            0  # Result to store the length of the longest substring
        )

        for right, char in enumerate(
            s,
        ):  # right is the right boundary of the window
            # If the character is found in the map and the last index is
            # within the current window
            if char in char_index_map and char_index_map[char] >= left:
                # Move the left boundary right after the previous occurrence
                # of the character
                left = char_index_map[char] + 1
            char_index_map[
                char
            ] = right  # Update the latest index of the character
            max_length = max(
                max_length,
                right - left + 1,
            )  # Calculate the window size and update the result if it's larger
        return max_length
