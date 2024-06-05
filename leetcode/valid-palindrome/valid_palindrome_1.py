class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphaNum(c: str) -> bool:
            return (
                ord("A") <= ord(c) <= ord("Z")
                or ord("a") <= ord(c) <= ord("z")
                or ord("0") <= ord(c) <= ord("9")
            )

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not alphaNum(s[left]):
                left += 1
            while left < right and not alphaNum(s[right]):
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True


solution = Solution()
print(solution.isPalindrome(s="A man, a plan, a canal: Panama"))
print(solution.isPalindrome(s="race a car"))
print(solution.isPalindrome(s=" "))
