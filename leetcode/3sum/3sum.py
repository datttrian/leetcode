class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets: list[list[int]] = []
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in triplets:
                            triplets.append(triplet)

        return triplets


solution = Solution()
print(solution.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
print(solution.threeSum(nums=[0, 1, 1]))
print(solution.threeSum(nums=[0, 0, 0]))
