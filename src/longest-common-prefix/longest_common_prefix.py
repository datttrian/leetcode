from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        # Sort the list of strings to bring similar prefixes together
        strs.sort()

        # Take the first and last strings after sorting
        first_str = strs[0]
        last_str = strs[-1]

        common_prefix: List[str] = []

        # Use enumerate to iterate through characters with their indices
        for i, char in enumerate(first_str):
            if i < len(last_str) and char == last_str[i]:
                common_prefix.append(char)
            else:
                break

        return ''.join(common_prefix)
