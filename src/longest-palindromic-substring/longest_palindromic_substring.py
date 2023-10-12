class Solution:
    def longestPalindrome(self, input_string: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while (
                left >= 0
                and right < len(input_string)
                and input_string[left] == input_string[right]
            ):
                left -= 1
                right += 1
            return input_string[left + 1 : right]

        longest_palindrome: str = ''
        for center in range(len(input_string)):
            palindrome1: str = expand_around_center(center, center)
            if len(palindrome1) > len(longest_palindrome):
                longest_palindrome = palindrome1
            palindrome2: str = expand_around_center(center, center + 1)
            if len(palindrome2) > len(longest_palindrome):
                longest_palindrome = palindrome2
        return longest_palindrome
