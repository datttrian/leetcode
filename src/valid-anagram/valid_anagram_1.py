class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for char in s:
            is_matched = False

            for i, c in enumerate(t):
                if c == char:
                    t = t[:i] + t[i + 1 :]
                    is_matched = True
                    break

            if not is_matched:
                return False

        return True


solution = Solution()
print(solution.isAnagram(s="anagram", t="nagaram"))
print(solution.isAnagram(s="rat", t="car"))
