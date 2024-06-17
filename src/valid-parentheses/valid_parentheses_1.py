class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        bracket_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            (
                stack.append(char)
                if char not in bracket_map
                else (
                    None
                    if stack and stack.pop() == bracket_map[char]
                    else stack.append(char)
                )
            )

        return not stack


solution = Solution()
print(solution.isValid(s="()"))  # True
print(solution.isValid(s="()[]{}"))  # True
print(solution.isValid(s="(]"))  # False
