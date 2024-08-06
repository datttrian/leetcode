from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:

        counts = Counter(word)

        queue = list(counts.values())
        queue.sort(reverse=True)

        push_count = 0

        for key, value in enumerate(queue):
            push_count += value

            if key >= 8:
                push_count += value

            if key >= 16:
                push_count += value

            if key >= 24:
                push_count += value

        return push_count
