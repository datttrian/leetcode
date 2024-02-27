class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Return the length of the last word in the string.

        Parameters:
        - s (str): The input string consisting of words and spaces.

        Returns:
        - int: The length of the last word.
        """
        # Remove trailing spaces
        s = s.rstrip()

        if not s:
            return 0

        # Find the last space index
        last_space_index = s.rfind(' ')

        if last_space_index == -1:
            return len(s)  # No space found, the entire string is the last word

        return len(s) - last_space_index - 1
