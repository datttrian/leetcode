class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        largest_k = -1
        for _, num in enumerate(nums):
            if num > 0:
                for _, num2 in enumerate(nums):
                    if num2 == -num:
                        if num > largest_k:
                            largest_k = num
                        break
        return largest_k
