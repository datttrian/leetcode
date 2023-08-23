from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "0": "",  # Empty string for '0'
            "1": "",  # Empty string for '1'
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # Initialize the queue with an empty string
        queue = [""]

        for digit in digits:
            next_queue = []
            for combination in queue:
                for letter in phone_map[digit]:
                    next_queue.append(combination + letter)
            queue = next_queue

        return queue
