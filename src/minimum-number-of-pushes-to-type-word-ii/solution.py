from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        queue = sorted(counts.values(), reverse=True)

        push_count = 0
        for i, value in enumerate(queue):
            multiplier = i // 8 + 1
            push_count += value * multiplier

        return push_count
