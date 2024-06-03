class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s: dict[str, int] = {}
        count_t: dict[str, int] = {}
        
        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1
        
        for char in t:
            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1
        
        for char in count_s:
            if char not in count_t or count_s[char] != count_t[char]:
                return False
        
        for char in count_t:
            if char not in count_s:
                return False
        
        return True


solution = Solution()
print(solution.isAnagram(s="anagram", t="nagaram"))
print(solution.isAnagram(s="rat", t="car"))
