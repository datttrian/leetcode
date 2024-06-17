class Solution:
    def isValid(self, s: str) -> bool:
        while any(pair in s for pair in ["()", "{}", "[]"]):
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
        return not s


solution = Solution()
print(solution.isValid(s="()"))
print(solution.isValid(s="()[]{}"))
print(solution.isValid(s="(]"))
