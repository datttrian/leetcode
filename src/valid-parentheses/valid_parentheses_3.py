class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        matching_parentheses = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in matching_parentheses:
                if not stack or stack.pop() != matching_parentheses[char]:
                    return False
            else:
                stack.append(char)
        return not stack


solution = Solution()
print(solution.isValid(s="()"))
print(solution.isValid(s="()[]{}"))
print(solution.isValid(s="(]"))
