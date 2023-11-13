from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        combinations = ['']  # start with an empty combination

        for digit in digits:
            new_combinations: List[str] = []
            for combination in combinations:
                for letter in phone_map[digit]:
                    new_combinations.append(combination + letter)
            combinations = new_combinations

        return combinations
