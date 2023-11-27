class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)

        # Check if the lengths of s1 and s2 add up to the length of s3
        if len_s1 + len_s2 != len_s3:
            return False

        # Initialize a 1D array to store the intermediate results
        dp = [False] * (len_s2 + 1)

        # Base case: an empty s1 and an empty s2 can form an empty s3
        dp[0] = True

        # Check if s1 and s3 can form s3
        for i in range(1, len_s2 + 1):
            dp[i] = dp[i - 1] and s2[i - 1] == s3[i - 1]

        # Check if s1 and s2 can form s3
        for i in range(1, len_s1 + 1):
            # Update the first element of dp for the current row
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            # Update dp for the rest of the row
            for j in range(1, len_s2 + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (
                    dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                )

        return dp[len_s2]
