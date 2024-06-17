class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        n = len(s)
        i = 0

        while i < n - 1:
            if (
                (s[i] == "(" and s[i + 1] == ")")
                or (s[i] == "{" and s[i + 1] == "}")
                or (s[i] == "[" and s[i + 1] == "]")
            ):
                new_s = s[:i] + s[i + 2 :]
                return self.isValid(new_s)
            i += 1

        return False
