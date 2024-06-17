class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        n = len(s)
        i = 0
        matching_parentheses = {"(": ")", "{": "}", "[": "]"}

        while i < n - 1:
            if s[i] in matching_parentheses and s[i + 1] == matching_parentheses[s[i]]:
                new_s = s[:i] + s[i + 2 :]
                return self.isValid(new_s)
            i += 1

        return False


solution = Solution()
print(solution.isValid(s="()"))
print(solution.isValid(s="()[]{}"))
print(solution.isValid(s="(]"))
