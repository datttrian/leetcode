class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map: dict[str, int] = {}

        left: int = 0

        max_length: int = 0

        for right, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1

            char_index_map[char] = right

            max_length = max(max_length, right - left + 1)

        return max_length
