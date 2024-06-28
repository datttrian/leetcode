from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        queue: deque[str] = deque()
        matching_parentheses = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in matching_parentheses:
                if not queue or queue.pop() != matching_parentheses[char]:
                    return False
            else:
                queue.append(char)

        return not queue


solution = Solution()
print(solution.isValid(s="()"))
print(solution.isValid(s="()[]{}"))
print(solution.isValid(s="(]"))
