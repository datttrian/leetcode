class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring in the given string.

        This algorithm, using the Expand Around Center technique, considers
        each index in the string as the middle of a potential palindrome
        and expands outwards checking for palindrome conditions. It expands
        around each character (for odd-length palindromes) and each pair of
        consecutive characters (for even-length palindromes), updating the
        longest palindrome found.


        Args:
            s (str): The input string to search for the palindrome.

        Returns:
            str: The longest palindromic substring in the input string.

        Complexity:
            Time: O(n^2), where n is the length of the input string. This time
            complexity arises from the fact that for each of the n characters,
            the expansion could potentially go through the rest of the string.

            Space: O(1), as the space used does not depend on the size of the
            input string and only a constant amount of extra space is used.
        """
        res = ''  # The result string to hold the longest palindrome found
        resLen = 0  # The length of the longest palindrome found

        for i in range(len(s)):
            # Check for palindrome of odd length by setting both left and
            # right pointers at i
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1  # Expand to the left
                r += 1  # Expand to the right

            # Check for palindrome of even length by setting left at i and
            # right at i + 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                l -= 1  # Expand to the left
                r += 1  # Expand to the right

        return res  # Return the longest palindrome
