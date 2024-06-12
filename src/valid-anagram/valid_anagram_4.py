class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count: dict[str, int] = {}

        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False

        for char, cnt in count.items():
            if cnt != 0:
                return False

        return True


solution = Solution()
print(solution.isAnagram(s="anagram", t="nagaram"))
print(solution.isAnagram(s="rat", t="car"))
