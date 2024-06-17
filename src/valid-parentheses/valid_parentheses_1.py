class Solution:
    def isValid(self, s: str) -> bool:
        matching_parentheses = ["()", "{}", "[]"]
        while any(pair in s for pair in matching_parentheses):
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
        return not s


solution = Solution()
print(solution.isValid(s="()"))
print(solution.isValid(s="()[]{}"))
print(solution.isValid(s="(]"))
