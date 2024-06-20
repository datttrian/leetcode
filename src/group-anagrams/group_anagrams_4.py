class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
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

        anagrams: dict[int, list[str]] = {}

        for word in strs:
            product = 1
            for char in word:
                product *= prime_numbers[char]

            if product in anagrams:
                anagrams[product].append(word)
            else:
                anagrams[product] = [word]

        return list(anagrams.values())


solution = Solution()
print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams(strs=[""]))
print(solution.groupAnagrams(strs=["a"]))
