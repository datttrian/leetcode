from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = sum(char // 2 * 2 for char in count.values())
        return length + any(char % 2 for char in count.values())
