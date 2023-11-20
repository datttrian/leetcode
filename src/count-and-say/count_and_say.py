import re


class Solution:
    def countAndSay(self, n: int) -> str:
        s: str = '1'
        for _ in range(n - 1):
            s = ''.join(
                str(len(group)) + digit
                for group, digit in re.findall(r'((.)\2*)', s)  # type: ignore
            )  # type: ignore
        return s
