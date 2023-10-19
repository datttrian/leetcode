class Solution:
    def isValid(self, s: str) -> bool:
        paren = []
        for c in s:
            if c in '({[':
                paren.append(c)
            elif c == ')':
                if not paren or paren[-1] != '(':
                    return False
                paren.pop()
            elif c == '}':
                if not paren or paren[-1] != '{':
                    return False
                paren.pop()
            elif c == ']':
                if not paren or paren[-1] != '[':
                    return False
                paren.pop()
            else:
                pass  # Handle other characters, if necessary
        return not paren
