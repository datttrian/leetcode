from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = len(words) * word_len
        word_count = Counter(words)
        result: List[int] = []

        for i in range(word_len):
            left, right = i, i
            current_count: Counter[str] = Counter()

            while right + word_len <= len(s):
                current_word = s[right : right + word_len]
                current_count[current_word] += 1
                right += word_len

                while current_count[current_word] > word_count[current_word]:
                    left_word = s[left : left + word_len]
                    current_count[left_word] -= 1
                    left += word_len

                if right - left == total_len:
                    result.append(left)

        return result
