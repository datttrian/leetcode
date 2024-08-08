class Solution:
    def isValid(self, s: str) -> bool:
        matching_parentheses = {"(": ")", "{": "}", "[": "]"}
        while any(open_paren + close_paren in s for open_paren, close_paren in matching_parentheses.items()):
            for open_paren, close_paren in matching_parentheses.items():
                s = s.replace(open_paren + close_paren, "")
        return not s


solution = Solution()
print(solution.isValid(s="()"))
print(solution.isValid(s="()[]{}"))
print(solution.isValid(s="(]"))
