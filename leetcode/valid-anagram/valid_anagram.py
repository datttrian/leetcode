class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26
        a_ord = ord("a")

        for char in s:
            counts[ord(char) - a_ord] += 1

        for char in t:
            counts[ord(char) - a_ord] -= 1
            if counts[ord(char) - a_ord] < 0:
                return False

        return True
