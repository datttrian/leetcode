class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        length = len(s)
        index = 0
        matching_parentheses = {"(": ")", "{": "}", "[": "]"}
        while index < length - 1:
            for open_paren, close_paren in matching_parentheses.items():
                if s[index] == open_paren and s[index + 1] == close_paren:
                    new_string = s[:index] + s[index + 2:]
                    return self.isValid(new_string)
            index += 1
        return False


solution = Solution()
print(solution.isValid(s="()"))
print(solution.isValid(s="()[]{}"))
print(solution.isValid(s="(]"))
