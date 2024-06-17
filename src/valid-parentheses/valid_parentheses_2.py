class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        bracket_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else "#"
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack


solution = Solution()
print(solution.isValid(s="()"))
print(solution.isValid(s="()[]{}"))
print(solution.isValid(s="(]"))
