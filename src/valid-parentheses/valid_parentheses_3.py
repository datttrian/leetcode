class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        bracket_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in bracket_map:
                if not stack or stack.pop() != bracket_map[char]:
                    return False
            else:
                stack.append(char)

        return not stack


solution = Solution()
print(solution.isValid(s="()"))
print(solution.isValid(s="()[]{}"))
print(solution.isValid(s="(]"))
