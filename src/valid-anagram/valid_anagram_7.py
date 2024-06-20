class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        prime_numbers = {
            "a": 2,
            "b": 3,
            "c": 5,
            "d": 7,
            "e": 11,
            "f": 13,
            "g": 17,
            "h": 19,
            "i": 23,
            "j": 29,
            "k": 31,
            "l": 37,
            "m": 41,
            "n": 43,
            "o": 47,
            "p": 53,
            "q": 59,
            "r": 61,
            "s": 67,
            "t": 71,
            "u": 73,
            "v": 79,
            "w": 83,
            "x": 89,
            "y": 97,
            "z": 101,
        }

        product_s = 1
        for char in s:
            product_s *= prime_numbers[char]

        product_t = 1
        for char in t:
            product_t *= prime_numbers[char]

        return product_s == product_t


solution = Solution()
print(solution.isAnagram(s="anagram", t="nagaram"))
print(solution.isAnagram(s="rat", t="car"))
