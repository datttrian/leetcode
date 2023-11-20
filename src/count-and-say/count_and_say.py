import itertools


class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'
        for _ in range(n - 1):
            v = ''
            for digit, group in itertools.groupby(result):
                count = len(list(group))
                v += '%i%s' % (count, digit)
            result = v

        return result
