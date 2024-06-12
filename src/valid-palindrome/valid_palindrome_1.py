class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_s = "".join(char.lower() for char in s if char.isalnum())
        return normalized_s == normalized_s[::-1]


solution = Solution()
print(solution.isPalindrome(s="A man, a plan, a canal: Panama"))
print(solution.isPalindrome(s="race a car"))
print(solution.isPalindrome(s=" "))
