class Solution:
    def isNumber(self, s: str) -> bool:
        num, exp, sign, dec = False, False, False, False
        for c in s:
            if '0' <= c <= '9':
                num = True
            elif c in ('e', 'E'):
                if exp or not num:
                    return False
                exp, num, sign, dec = True, False, False, False
            elif c in ('+', '-'):
                if sign or num or dec:
                    return False
                sign = True
            elif c == '.':
                if dec or exp:
                    return False
                dec = True
            else:
                return False
        return num
