class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count: dict[str, int] = {}

        for i, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1

        for _, value in count.items():
            if value != 0:
                return False

        return True


solution = Solution()
print(solution.isAnagram(s="anagram", t="nagaram"))
print(solution.isAnagram(s="rat", t="car"))
