from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Find the longest common prefix among a list of strings.

        This function takes a list of strings as input and returns the longest
        common prefix shared among all strings. The input list is sorted to
        bring similar prefixes together, and the common prefix is determined
        by comparing the characters at each position in the first and last
        strings after sorting.

        Parameters:
        - strs (List[str]): A list of strings for which the common prefix
        needs to be found.

        Returns:
        - str: The longest common prefix of the input strings. If the input
        list is empty, an empty string is returned.

        Raises:
        - None

        Complexity:
        - Time: O(n * m * log(n)), where n is the number of strings in the
        input list, and m is the average length of the strings. The sorting
        step dominates the time complexity.
        - Space: O(m), where m is the length of the common prefix. The space
        complexity is determined by the list storing the common prefix
        characters.
        """
        # Check if the input list is empty
        if not strs:
            return ''

        # Sort the list of strings to bring similar prefixes together
        strs.sort()

        # Take the first and last strings after sorting
        first_str = strs[0]
        last_str = strs[-1]

        # Initialize an empty list to store the common prefix characters
        common_prefix: List[str] = []

        # Use enumerate to iterate through characters with their indices
        for i, char in enumerate(first_str):
            # Check if the current index is within the length of the last
            # string and if the character matches between the first and last
            # strings
            if i < len(last_str) and char == last_str[i]:
                common_prefix.append(char)
            else:
                # Break the loop if there is a mismatch, indicating the end of
                # the common prefix
                break

        # Join the list of common prefix characters into a single string and
        # return
        return ''.join(common_prefix)
