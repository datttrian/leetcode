from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)
        length = sum(count // 2 * 2 for count in char_count.values())
        return length + any(count % 2 for count in char_count.values())
