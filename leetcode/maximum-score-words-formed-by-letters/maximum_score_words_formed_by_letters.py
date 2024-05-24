from collections import Counter


class Solution:
    def maxScoreWords(
        self, words: list[str], letters: list[str], score: list[int]
    ) -> int:
        letter_counts: Counter[str] = Counter(letters)

        score_dict: dict[str, int] = {
            chr(97 + i): score[i] for i in range(len(score))
        }

        word_scores: dict[str, int] = {
            word: sum(score_dict[char] for char in word) for word in words
        }

        def can_form_words(
            words: list[str], letter_counts: Counter[str]
        ) -> bool:
            temp_letter_counts = letter_counts.copy()
            for word in words:
                word_count = Counter(word)
                for char in word_count:
                    if temp_letter_counts[char] < word_count[char]:
                        return False
                    temp_letter_counts[char] -= word_count[char]
            return True

        max_score: int = 0
        n: int = len(words)

        for mask in range(1 << n):
            current_words: list[str] = [
                words[i] for i in range(n) if mask & (1 << i)
            ]
            if can_form_words(current_words, letter_counts):
                current_score: int = sum(
                    word_scores[word] for word in current_words
                )
                max_score = max(max_score, current_score)

        return max_score


solution = Solution()
words = ["dog", "cat", "dad", "good"]
letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
score = [
    1,
    0,
    9,
    5,
    0,
    0,
    3,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    2,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]
print(solution.maxScoreWords(words, letters, score))
