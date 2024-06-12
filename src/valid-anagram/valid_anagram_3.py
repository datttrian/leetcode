class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s: dict[str, int] = {}
        count_t: dict[str, int] = {}

        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        for char, count in count_s.items():
            if count_t.get(char, 0) != count:
                return False

        return len(count_s) == len(count_t)


solution = Solution()
print(solution.isAnagram(s="anagram", t="nagaram"))
print(solution.isAnagram(s="rat", t="car"))
