class Solution:
    def myAtoi(self, s: str) -> int:
        length = len(s)
        num = 0
        i = 0
        
        while i < length and s[i] == ' ':
            i += 1
        
        if i < length and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        else:
            sign = 1
        
        while i < length and '0' <= s[i] <= '9':
            num = num * 10 + (ord(s[i]) - ord('0'))
            i += 1
        
        num *= sign
        
        num = min(num, 2**31 - 1)
        num = max(num, -2**31)
        
        return num
