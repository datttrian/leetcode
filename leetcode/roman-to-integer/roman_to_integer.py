class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        for i, current_char in enumerate(s):
            if i + 1 < len(s) and roman[current_char] < roman[s[i + 1]]:
                res -= roman[current_char]
            else:
                res += roman[current_char]
        return res
