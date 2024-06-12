class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums_set = set(nums)
        largest_k = -1

        for num in nums:
            if num > 0 and -num in nums_set:
                largest_k = max(largest_k, num)

        return largest_k
