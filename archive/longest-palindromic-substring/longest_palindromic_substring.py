class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindrome in a given string.

        Parameters:
        - s (str): The input string for which the longest palindrome needs to
        be found.

        Returns:
        - str: The longest palindrome found in the input string.

        Raises:
        - None
        """
        # String to hold the longest palindrome found
        res = ''

        # The length of the longest palindrome found
        resLen = 0

        for i in range(len(s)):
            # For each character in the string, attempt to find the longest
            # palindrome with the character as the center for odd-length
            # palindromes.
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If the currently considered substring is a palindrome
                # (indicated by the equality of characters at positions l and
                # r), and if its length is greater than the length of the
                # previously recorded longest palindrome, then update the
                # result and the length of the result
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                # Expand the considered range to the left and right
                l -= 1
                r += 1

            # After checking for odd-length palindromes with center `i`, check
            # for even-length palindromes by considering the center to be
            # between `i` and `i+1`.
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Similar to the odd-length palindrome check, update the
                # result and its length if a longer palindrome is found.
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                # Expand the considered range to the left and right
                l -= 1
                r += 1

        # After checking all characters and all possible centers for
        # palindromes, return the longest palindrome found in the string.
        return res
