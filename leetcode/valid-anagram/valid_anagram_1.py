class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for char in s:
            is_found = False
            for i in range(len(t)):
                if t[i] == char:
                    t = t[:i] + t[i + 1 :]
                    is_found = True
                    break

            if not is_found:
                return False

        return True


solution = Solution()
print(solution.isAnagram(s="anagram", t="nagaram"))
print(solution.isAnagram(s="rat", t="car"))
