class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        n = len(s)
        i = 0
        matching_parentheses = [("(", ")"), ("{", "}"), ("[", "]")]

        while i < n - 1:
            for opening, closing in matching_parentheses:
                if s[i] == opening and s[i + 1] == closing:
                    new_s = s[:i] + s[i + 2 :]
                    return self.isValid(new_s)
            i += 1

        return False


solution = Solution()
print(solution.isValid(s="()"))
print(solution.isValid(s="()[]{}"))
print(solution.isValid(s="(]"))
