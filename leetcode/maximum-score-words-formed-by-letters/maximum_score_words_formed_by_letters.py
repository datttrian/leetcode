from itertools import combinations


class Solution:
    def maxScoreWords(
        self, words: list[str], letters: list[str], score: list[int]
    ) -> int:
        letter_counts: dict[str, int] = {}
        for letter in letters:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1

        score_dict: dict[str, int] = {
            chr(97 + i): score[i] for i in range(len(score))
        }

        def generate_subsets(words: list[str]) -> list[list[str]]:
            subsets: list[list[str]] = []
            for i in range(len(words) + 1):
                for combo in combinations(words, i):
                    subsets.append(list(combo))
            return subsets

        def calculate_word_score(word: str, score_dict: dict[str, int]) -> int:
            return sum(score_dict[char] for char in word)

        def can_form_words(
            words: list[str], letter_counts: dict[str, int]
        ) -> bool:
            temp_letter_counts = letter_counts.copy()
            for word in words:
                for char in word:
                    if temp_letter_counts.get(char, 0) == 0:
                        return False
                    temp_letter_counts[char] -= 1
            return True

        all_subsets: list[list[str]] = generate_subsets(words)
        max_score = 0

        for subset in all_subsets:
            if can_form_words(subset, letter_counts):
                subset_score = sum(
                    calculate_word_score(word, score_dict) for word in subset
                )
                max_score = max(max_score, subset_score)

        return max_score
